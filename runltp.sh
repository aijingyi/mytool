#! /bin/bash

 

groups="admin_tools cap_bounds commands connectors containers dio fcntl-locktests filecaps fs fs_perms_simple io ipc kernel_misc math mm modules nptl pty sched syscalls timers"

# standard mode - kernel_misc cause system reboot.

# groups="math mm modules nptl pty sched syscalls timers"

for test in $groups

do

    echo "start LTP $test ..."

    /opt/ltp/wrLinux_ltp/wr-runltp -f ${test} | tee /root/ltp_${test}.txt

    echo "cat /opt/ltp/wrLinux_ltp/results/LTP.log" >> /root/ltp_${test}.txt

    cat /opt/ltp/wrLinux_ltp/results/LTP.log >> /root/ltp_${test}.txt

done

 

groups="AIO MEM MSG SEM SIG THR TMR TPS"

 

for test in $groups

do

    echo "start POSIX $test ..."

    /opt/open_posix_testsuite/wrLinux_posix/wr-runposix -f ${test} | tee /root/posix_${test}.txt

    echo "cat /opt/open_posix_testsuite/wrLinux_posix/results/POSIX.log" >> /root/posxi_${test}.txt

    cat /opt/open_posix_testsuite/wrLinux_posix/results/POSIX.log >> /root/posix_${test}.txt

done
