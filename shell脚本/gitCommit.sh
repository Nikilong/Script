echo '请输入代码的路径,默认为(/Users/admin/Documents/code/Personal),按下Enter采取默认'
# read为等待用户输入
read path
if [ ! $path ]; then
    path='/Users/admin/Documents/code/Personal'
fi
echo $path
cd $path
if [ -d $path ]; then
    #删除.DS_Store
    find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
    git status
    echo '等待输入' && read inpu
    git add .
    git commit -m $1
    echo '等待输入' && read inpu
    git pull --rebase origin master
    echo '等待输入' && read inpu
    git push -u origin master
else
    echo '文件路径不存在'
fi

