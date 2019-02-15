/*
现在有一种字符串的压缩规则是这样的：k[string]
表示 string 连续出现 k 次（0 < k < 1000）。
比如：s = "ef3[a]2[bc]gh", 解压后的字符串为： "efaaabcbcgh"
这种压缩也可以相互嵌套：s = "3[a2[c]]",
解压后为： "accaccacc" 输入一个压缩的字符串 s，请输出解压后的字符串。
输入都是严格合法的，数字只用来表示重复次数，不会出现 3a 或者 2[4]这样的输入
解压后的字符串只有字母。
*/
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func getstring(a int, str string) string {
	return strings.Repeat(str, a)
}

func unzip(str string) string {
	var ipos []int
	var value []byte
	var strvalue []string
	for i := 0; i < len(str); i++ {
		if str[i] >= '0' && str[i] <= '9' {
			value = append(value, str[i])
		} else if str[i] == '[' {
			strvalue = append(strvalue, string(value[:]))
			value = []byte{}
			ipos = append(ipos, i+1)
		} else if str[i] == ']' {
			n, _ := strconv.Atoi(strvalue[len(strvalue)-1])
			tmpres := getstring(int(n), str[ipos[len(ipos)-1]:i])
			ilen := len(str[ipos[len(ipos)-1]-2 : i+1])
			str = strings.Replace(str, str[ipos[len(ipos)-1]-2:i+1], tmpres, 1)
			i = i + len(tmpres) - ilen
			strvalue = strvalue[0 : len(strvalue)-1]
			ipos = ipos[0 : len(ipos)-1]
			continue
		}
	}
	return str
}

func unziptest() {
	str := "ef3[a]2[bc]gh2[a]"
	//str := "3[a2[c]]"
	//fmt.Scanln(&str)
	str = unzip(str)
	fmt.Println(str)
}
