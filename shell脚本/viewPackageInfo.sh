#!/bin/bash
root_path=$1

if [ -d $root_path/iOS ]; then
    echo -e '\n--------addLibs.txt---------'
    cat $root_path/iOS/addLibs.txt
    echo -e '\n--------removeLibs.txt---------'
    cat $root_path/iOS/removeLibs.txt
    echo -e '\n--------exoa_mobile-Info.plist---------'
    cat $root_path/iOS/exoa_mobile-Info.plist
    echo -e '\n--------PackageDefine.h---------'
    cat $root_path/iOS/PackageDefine.h
    echo -e '\n--------initConfig.xml---------'
    cat $root_path/iOS/initConfig.xml
    echo -e '\n=========重要信息========='
    echo -e '\n********Address*****'
    echo `grep '<serverAddress' $root_path/iOS/initConfig.xml `
    echo `grep '<vpnAddress' $root_path/iOS/initConfig.xml `
    echo `grep '_VPN' $root_path/iOS/PackageDefine.h `
    echo -e '\n********CFBundleDisplayName*****'
    /usr/libexec/PlistBuddy -c "Print CFBundleDisplayName"  $root_path/iOS/exoa_mobile-Info.plist
    echo -e '\n********iPhone X全面屏配置*****'
    /usr/libexec/PlistBuddy -c "Print UILaunchStoryboardName"  $root_path/iOS/exoa_mobile-Info.plist
    echo -e '\n=========end========='
    echo -e '目标文件夹:\n'$root_path'\n'
    #打开图片
    open $root_path/iOS/Icon-72@3x.png
else
    echo -e '该项目没有iOS配置文件夹'
    open $root_path
fi
