#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#FileName:webAppPackage.py

import os
import time

pro = raw_input('project name(fl:妇联,gl:工联,jz:街总): ')
#pro = "gl"
pathSource = '/Users/Longcq/Documents/excellence_code/web上架/'
pathDen = '/Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient'
if pro == 'fl':
    pathSource = pathSource + 'am_澳门web项目婦女聯合總會'
    uuid = "84f6c800-1da5-4c75-ada8-bf104577ec55"
    cerName = "amgldev_provisioning_profile"
    developTeam = "MTLQGK7TKX"
    bundleID = "com.excellence.webclient.gldev"
elif pro == 'gl':
    pathSource = pathSource + 'am_澳门web项目工會聯合總會'
    uuid = "84f6c800-1da5-4c75-ada8-bf104577ec55"
    cerName = "amgldev_provisioning_profile"
    developTeam = "MTLQGK7TKX"
    bundleID = "com.excellence.webclient.gldev"
elif pro == 'jz':
    pathSource = pathSource + 'am_澳门web项目街坊會聯合總會'
    uuid = "84f6c800-1da5-4c75-ada8-bf104577ec55"
    cerName = "amgldev_provisioning_profile"
    developTeam = "MTLQGK7TKX"
    bundleID = "com.excellence.iExOA3"


order = '''
    cp %s/source.zip %s/Config/source.zip ;
    cp %s/PackageDefine.h %s/Networks/EXGetDataLib/publicDefine/PackageDefine.h ;
    cp %s/Info.plist %s/Info.plist ;
    cp -r -f %s/AppIcon.appiconset %s/Images.xcassets
    cp -r -f %s/icons %s
    
    '''%((pathSource,pathDen) * 5)


#undo
#sed -i ""  s/''/''/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj;
#proSet = '''
#    #取消使用自动签名
#    sed -i ""  s/'ProvisioningStyle = Automatic;'/'ProvisioningStyle = Manual;'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #uuid
#    sed -i ""  s/'PROVISIONING_PROFILE = "";'/'PROVISIONING_PROFILE = "%s";'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #配置证书uuid，PROVISIONING_PROFILE=证书的uuid
#    #'PROVISIONING_PROFILE_SPECIFIER证书名
#    sed -i ""  s/'PROVISIONING_PROFILE_SPECIFIER = "";'/'PROVISIONING_PROFILE_SPECIFIER = %s;'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #替换签名证书
#    #sed -i ""  s/'"CODE_SIGN_IDENTITY\[sdk=iphoneos\*\]" = "iPhone Developer";'/'"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone Distribution: Excellence Information Technology Corp., Ltd.";'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #推送和keychain
#    sed -i ""  s/'com.apple.Keychain = {*enabled = 0;};'/'com.apple.Keychain = {enabled = 1;};'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    sed -i ""  s/'com.apple.Push = {*enabled = 0;};'/'com.apple.Push = {enabled = 1;};'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #证书开发者组id
#    #sed -i ""  s/'DEVELOPMENT_TEAM = "S3RSD3BB8U";'/'DEVELOPMENT_TEAM = "%s";'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#    #修改bundle ID
#    sed -i ""  s/'PRODUCT_BUNDLE_IDENTIFIER = com.excellence.webclient;'/'PRODUCT_BUNDLE_IDENTIFIER = %s;'/g /Users/Longcq/Documents/excellence_code/iExWebClient/iExWebClient.xcodeproj/project.pbxproj;
#
#'''%(uuid,cerName,developTeam,bundleID)


print order

if os.system(order) == 0:
    print '----->>>success<<<-----\n'
else:
    print '----->>>failed<<<------\n'

