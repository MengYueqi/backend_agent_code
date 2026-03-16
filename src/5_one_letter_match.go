package src

// 题目：查询是否存在只修改一个字母即可匹配的单词
type Trie struct {
	next   []*Trie
	isLast bool
}

func initTrie() Trie {
	return Trie{
		isLast: false,
		next:   make([]*Trie, 26),
	}
}

func (this *Trie) addWord(word string) {
	curNode := this
	for i := 0; i < len(word); i++ {
		if curNode.next[word[i]-'a'] == nil {
			curNode.next[word[i]-'a'] = &Trie{
				isLast: false,
				next:   make([]*Trie, 26),
			}
			curNode = curNode.next[word[i]-'a']
		} else {
			curNode = curNode.next[word[i]-'a']
		}
	}
	curNode.isLast = true
}

func (this *Trie) findWord(word string) bool {
	curNode := this
	for i := 0; i < len(word); i++ {
		if curNode.next[word[i]-'a'] == nil {
			return false
		}
		curNode = curNode.next[word[i]-'a']
	}
	return curNode.isLast
}

func HasOneLetterDifference(words []string, x string) bool {
	// TODO: implement
	trie := initTrie()
	for i := 0; i < len(words); i++ {
		for j := 0; j < len(words[i]); j++ {
			prevWord := []byte(words[i])
			for k := 0; k < 26; k++ {
				prevWord[j] = byte('a' + k)
				if string(prevWord) != words[i] {
					trie.addWord(string(prevWord))
				}
			}
		}
	}
	return trie.findWord(x)
}
