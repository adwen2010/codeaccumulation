# codeaccumulation
codeaccumulation 
#one.go
现在有一种字符串的压缩规则是这样的：k[string]
表示 string 连续出现 k 次（0 < k < 1000）。
比如：s = "ef3[a]2[bc]gh", 解压后的字符串为： "efaaabcbcgh"
这种压缩也可以相互嵌套：s = "3[a2[c]]",
解压后为： "accaccacc" 输入一个压缩的字符串 s，请输出解压后的字符串。
输入都是严格合法的，数字只用来表示重复次数，不会出现 3a 或者 2[4]这样的输入
解压后的字符串只有字母。
