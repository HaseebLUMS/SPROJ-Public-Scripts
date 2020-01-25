/*
	Keywords Extractor for Rule-Based Classifier
	proposed by JSCleaner.
*/
package main

import (
	"fmt"
	"path/filepath"
	"io"
	"io/ioutil"
	"os"
	"bufio"
	"sort"
	"encoding/json"
	"strings"
	"regexp"
)

const FILELIMIT = 200

func allIndices(content string, target string) []int{
	var res = []int{}
	if (len(content) < 1) || (len(target) < 1){
		return res
	}
	lt := len(target)
	end := len(content)-lt+1;
	for i:=0; i < end; i++{
		if content[i:i+lt] == target{
			res = append(res, i)
		}
	}
	return res
}

func extractKeywords(content string, features []string) []string{

	space := regexp.MustCompile(`\s+`)
	content = space.ReplaceAllString(content, " ")

	result := make([]string, 0)
	keys := make([]int, 0)
	tmp := make(map[int]string)
	for i := 0; i < len(features); i++{
		target0 := "."+features[i]+"("
		target1 := "."+features[i]+" ("
		res := allIndices(content, target0)
		res = append(res, (allIndices(content, target1))...)
		keys = append(keys, res...)
		for j := 0; j < len(res); j++{
			tmp[res[j]] = features[i]
		}
	}
	sort.Ints(keys)
	for _, k := range(keys){
		result = append(result, tmp[k])
	}
	return result
}

func handleFolder(folder string, features []string) {
	fileNames, err := filepath.Glob(folder+"/*")
	if err != nil {
		fmt.Println(err.Error())
	}
	if len(fileNames) < 1{
		return
	}
	
	kws := make(map[string][]string)
	for i:= 0; i < len(fileNames); i++{
		file := fileNames[i]
		data, err := ioutil.ReadFile(file)
		if err != nil{
			fmt.Println(err.Error())
		}
		content := string(data)
		words := extractKeywords(content, features)
		kws[file] = words
	}
	j, err := json.Marshal(kws)
	if err != nil {
		fmt.Println(err.Error())
	}
	d := []byte(j)
	res1 := strings.Split(folder, "/")
	fn := res1[len(res1)-1]
    err = ioutil.WriteFile("tmp/"+fn+".json", d, os.ModePerm)
    if err != nil{
    	fmt.Println(err.Error())
    }
    return
}

func readFeatures() []string{
	res := make([]string, 0)
    f, err := os.OpenFile("./features", os.O_RDONLY, os.ModePerm)
    if err != nil {
    	fmt.Println(err.Error())
        return res
    }
    defer f.Close()

    rd := bufio.NewReader(f)
    for {
        line, err := rd.ReadString('\n')
        if err != nil {
            if err == io.EOF {
                break
            }
            fmt.Println(err.Error())
            return res
        }
        // _ = line  // GET the line string
        feature := line[:len(line)-1]
        res = append(res, feature)
    }
    return res
}
func superVisor(folderNames []string) {
	features := readFeatures()
	_ = features
	fmt.Println(len(features), " features read.")
	done := make(chan int, FILELIMIT)
	for i:= 0; i < len(folderNames); i++{
		fmt.Println(i)
		done <- 1
		go func(folder string){
			handleFolder(folder, features)
			<-done
		}(folderNames[i])
	}
	for{
		fmt.Println(".")
		if len(done) == 0{
			break
		}
	}
	fmt.Println("superVisor leaving...")
}

func main() {
	folderNames, err := filepath.Glob("./data/*")
	if err != nil {
		fmt.Println(err.Error())
	}
	superVisor(folderNames)
	fmt.Println("End.")
	return
}
