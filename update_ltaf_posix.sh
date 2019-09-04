#!/bin/bash

eval test_suites=($(ls posix_*.txt | cut -d "." -f 1 | xargs))
test_suites_num=${#test_suites[@]}
echo ${test_suites[*]} : $test_suites_num

[ -s template_posix ] || { echo "Not find template_ltp " ; exit -1; }

upload_subcase()
{
    t_case_name=$1
    t_status=$2
    if [ "X${t_status}" = "XUNTESTED" ]; then
        t_status=PASS
    fi
    if [ "X${t_status}" = "XUNSUPPORTED" ]; then
        t_status=PASS
    fi
    if [ "X${t_status}" = "XUNRESOLVED" ]; then
        t_status=PASS
    fi
    if [ "X${t_status}" = "XHUNG" ]; then
        t_status=Fail
    fi
    if [ "X${t_status}" = "XSIGNALED" ]; then
        t_status=Fail
    fi

    echo "Create testcase.ini for $test_suite : $t_case_name : $t_status..."
    sed -e "s/TEST_NAME/$t_case_name/g" -e " s/TEST_SUITE/$test_suite/g" -e "s/STATUS/$t_status/g" template_posix > testcase.ini
    
    curl -F resultfile=@/${PWD}/testcase.ini http://pek-lpgtest3.wrs.com/ltaf/upload_results.php    

    logpath=$(grep "log = " testcase.ini | cut -d " " -f 3) 
    echo "Upload log to $logpath ..." 
    mkdir -p $logpath
    chmod 777 $logpath
    cp $test_suite.txt $logpath
    chmod 777 ${logpath}/${test_suite}.txt
    rm -rf testcase.ini
}


for i in $(seq $test_suites_num ) ;
do
    test_suite=${test_suites[$((i-1))]}
    echo -e "\nStart : $i : $test_suite ...\n"
  
    ############################################
    ######STEP 1           #####################
    ############################################
    record=0
    record_S=0
    index=1
    rm ./temp
    sub_case_name=()
    sub_case_result=()
    while read line
    do
        if [ $record -eq 1 ]; then
            if [ $record_S -eq 1 ]; then
                if ( echo $line | grep -q "\-\-\-\-\-\-\-\-\-\-\-" ) ; then
                    record_S=0
                    continue
                fi
                if ( echo $line | grep -q "execution" ) ; then
                    :
                else
                    continue
                fi
                temp_path=$(echo $line | cut -d ":" -f 1)
                sub_case_name[$index]=$(basename $temp_path)  # tested subcase of posix
                temp_result=$(echo $line | cut -d ":" -f 3)
                sub_case_result[$index]=$(echo $temp_result)  # results of tested subcase of posix
                index=$(($index+1))
            else
                echo $line >> ./temp
            fi            
            continue
        fi        
        if ( echo $line | grep "POSIX Test Start Time" ) ; then
            record=1
            record_S=1
            read line
        fi        
    done < ${test_suite}.txt

    ############################################
    ######STEP 2           #####################
    ############################################
    sub_case_name_num=${#sub_case_name[@]}
    sub_case_result_num=${#sub_case_name[@]}
    if ! [ $sub_case_name_num -eq $sub_case_result_num ]; then
        echo "Test summary number wrong :$sub_case_name_num --- $sub_case_result_num "
        exit 0
    fi
    
    for i in $(seq $sub_case_name_num)
    do
        if [ X${sub_case_name[$i]} = X"" ]; then
            continue
        fi
        if [ ${sub_case_result[$i]} = "FAILED" ]; then
            know_issue=$(grep ${sub_case_name[$i]} temp | cut -d " " -f 3)
            if ! [ X$know_issue = X"" ]; then
                sub_case_result[$i]="PASS"
            else
                sub_case_result[$i]="FAIL"
            fi
            
        fi
    done

    ############################################
    ######STEP 3           #####################
    ############################################
    record=0
    while read line
    do
        #if [ $record -eq 1 ]; then
         #   if ( echo $line | grep -q "SKIP" ) ; then
          #      sub_case_name[$index]=$(echo $line | cut -d " " -f 2 | cut -d "." -f 1)
           #     sub_case_result[$index]="PASS"
            #    index=$(($index+1))
           # fi
        #fi
        if ( echo $line | grep "POSIX Test Start Time" ) ; then
            record=1
        fi 
    done < ./temp
    
    ############################################
    ######STEP 4           #####################
    ############################################
    rm -rf temp
    
    sub_case_name_num=${#sub_case_name[@]}
    sub_case_result_num=${#sub_case_name[@]}
    if ! [ $sub_case_name_num -eq $sub_case_result_num ]; then
        echo "Test summary number wrong :$sub_case_name_num --- $sub_case_result_num "
    fi
    
    for i in $(seq $sub_case_name_num)
    do
        if [ X${sub_case_name[$i]} = X"" ]; then
            continue
        fi
        echo "$i / $sub_case_name_num: process ${sub_case_name[$i]} --${sub_case_result[$i]}"
        upload_subcase ${sub_case_name[$i]} ${sub_case_result[$i]}
    done
    
done



