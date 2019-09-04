

opt=$1


set_env()
{

    component=LTP
    component1=POSIX

    #release_name="WRLinux 10.17.41.x"
    #release_name="WRLinux 10.18"
    #release_name="WRLinux 10.18"
    release_name="WRLinux CD Next"
    #release_name="WRLinux sandbox"
    #release_name="Linux 9.0 RCPL"
    #release_name=PreUploads

    spin=GIT_20190903
    #spin="WRLINUX_10_17_LTS_RCPL0012"
    #spin="WRLINUX_10_18_LTS_RCPL0008"
    #sprint=WRL-10.18.44.8
    sprint="lx10.19 - S12"
    #sprint=WRL-9.0.0.20
    #sprint="Lx 10.18 - S13 - 2018-10-31"
    
    week=2019WW36
    #week=LX05

    bsp=intel-x86-64
    #bsp=nxp-ls1046
    #bsp=nxp-imx7
    #bsp=intel-skylake-avx512-64

    #kernel=preempt-rt
    kernel=standard

    #rootfs=glibc-cgl	
    #rootfs=glibc-std-sato	
    #rootfs=core-image-base
    #rootfs=glibc-std
    rootfs=glibc-std-xfce
    #rootfs=core-image-sato	

    multilib=
    init_type=systemd
    toolchain=OE
    tester=kliang
    target=CascadeLake
    #target=NUC7i5DNK1E
    #target=fsl_ls1046a_rdb	
    #target=intel_kabylake-R	
    #target=IOTG_Yuba_City	
    #target=SDP_Purley_2S
    #target=IMX6Quad-SD
    #target=IMX7D-SABRESD
    #target=IMX6SoloX-SDB
    #barcode=25079
    #barcode=21977
    barcode=25038
    #barcode=922009
    hostos=
    keywords=
    #keywords=nodistro
    extra_key=
    #extra_key=RAID1_USB_boot
    #extra_key=harddisk_boot
    #extra_key=
    #tags=Release
    tags=
    #requirements=US123456
    #requirements=LINUXEXEC-2653
    #requirements=LINUXEXEC-3008
    requirements=LINUXEXEC-3261
    #requirements=LINUXEXEC-2881
    #log_base_dir=/lpg-build/cdc/publiclog/
}

mk_upload_env()
{
    env_name=upload_env
    cat > $env_name <<EOF
release_name = $release_name
spin = $spin
sprint = $sprint
week = $week
bsp = $bsp
kernel = $kernel
rootfs = $rootfs
multilib = $multilib
init_type = $init_type
toolchain = $toolchain
tester = $tester
target = $target
barcode = $barcode
hostos = $hostos
keywords = $keywords
extra_key = $extra_key
tags = $tags
requirements = $requirements
log_base_dir=/lpg-build/cdc/publiclog/
EOF
}

mk_template()
{
    compo=$(echo $1 | tr '[A-Z]' '[a-z]')
    echo $compo
    cat > template_$compo << EOF
[LTAF]
action = add_update

release_name = $release_name

test_name = TEST_NAME
test_suite = TEST_SUITE
test_component = $1

sprint = $sprint
week = $week

bsp = $bsp
kernel = $kernel
rootfs = $rootfs
target = $target	
hostos = $hostos
keywords = $keywords
multilib = $multilib
#dtb = 
init_type = systemd
status = STATUS
log = /lpg-build/cdc/publiclog/`echo $release_name | sed  's/[ [ -]*//g'`/`echo $sprint | sed  's/ /-/g'`/$week/$spin/$1/${bsp}_${kernel}_$rootfs/
#tags = Release

spin = $spin	
toolchain = OE
barcode = $barcode

requirements = $requirements

wassp_env_id = CQ:WIND00465551::MYSQL1:4 
wassp_env_name = MYSQL1:4
wassp_rel_name = CQ:WIND00465551 
wassp_system = ${bsp}_${kernel}_$rootfs
wassp_system_label = ${target}-RevB3_OE_systemd

inherit_defect = yes
inherit_requirement = yes
EOF
}

upload_ltaf()
{
    #release_name=$wr_project_name
    #sprint=$sprint
    #week=$week
    #bsp=$bsp
    #kernel=$kernel
    #rootfs=$rootfs
    #target=$target
    #init_type=systemd
    #spin=$spin
    #tester=$tester
    #hostos=$hostos
    #multilib=$multilib
    #tags=$tags
    #barcode=$barcode 
    #requirements=$requirement
    #keywords= 
    #extra_key= 
    #testname=$testname
    #test_suite=$testname
    #test_component=$domain
    #status=PASS
    
    log="/lpg-build/cdc/publiclog/`echo $release_name | sed  's/[ [ -]*//g'`/`echo $sprint | sed  's/ /-/g'`/$week/$spin/$test_component/${bsp}_${kernel}_${rootfs}/${target}_OE_systemd/${testname}"
    
    mkdir -p $log
    
    
    cp -r ${testname}.log $log
    
    [ ! -d $log_path ] && mkdir -p $log_path
cat > ltaf_upload.ini <<EOF
[LTAF]
action = add_update
release_name = $release_name
sprint = $sprint
week = $week
bsp = $bsp
kernel = $kernel
rootfs = $rootfs
target = $target
init_type = $init_type
spin = ${spin}
toolchain = OE
tester = $tester
hostos = $host
multilib = $multilib
tags = $tags
barcode = $barcode
requirements = $requirements
keywords = $keywords
extra_key = $extra_key
testname = $testname
test_suite = $testname
test_component = $test_component
status = PASS
log = $log
inherit_defect = yes
inherit_requirement = yes
function_pass = 0
function_fail = 0
EOF

    echo "upload log to ltaf."
    curl -F resultfile=@ltaf_upload.ini http://pek-lpgtest3.wrs.com/ltaf/upload_results.php

}

set_env

if [ $opt = 'bts' ]; then 
    mk_upload_env
elif [ $opt = 'ltp' ]; then
    mk_template ltp
    mk_template posix
    
else 
   #echo "Please enter \"bts\" or \"ltp\""
   test_component=BSP
   testname=$opt
   upload_ltaf
fi
