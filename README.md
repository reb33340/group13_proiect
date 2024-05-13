## 記得每次commit之前先git pull
## How to pull request
1.使用git add \<file\> 將要文件加入要更新的版本  
2.使用git commit -m "訊息" 設定這個版本的註解  
3.使用git push 將版本推/送上雲端  
```
git add <file>
```
```
git commit -m "輸入你想說的訊息"
```
```
git push
```

## 解決merge conflict
1.如果遇到檔案重複更改
（就是改過檔案，然後你還沒git pull又改了的情況）
```
git pull --rebase
```
2.如果是git push之前忘記先git pull，無檔案衝突問題
```
git pull origin main --rebase
```

## 如何刪除檔案
在terminal刪除本機檔案
```
rm <file>
```
刪除github檔案
(和git add一樣，之後需要git commit和git push）
```
git rm <file>
```
同時刪除本機和github檔案(備註同上）
```
git rm -f <file>
```

## 如何進入docker
```
source docker_run.sh
```
退出 ctrl+D 或是
```
exit
```

## 上課教材
[Lab2](https://drive.google.com/file/d/1VbJf0k_hWzUK0Pw-tUSgQfn0Gb2w3_cm/view)
