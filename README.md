# leetcode刷题记录
***  
### 动态规划  
[刷题tag链接](https://zhuanlan.zhihu.com/p/126546914?utm_source=wechat_session&utm_medium=social&utm_oi=27134168924160%E3%80%82)  
*线性DP  
最长上升子序列 (LIS)，最长公共子序列 (LCS)

***  
## 字典树
Trie树，是一种树形结构，是一种哈希树的变种。典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。    
应用：串的快速检索，最长公共前缀（IP路由）    
常用操作：插入，查找，前缀匹配  
如下图：对于一个单词集合{'am','bad','be','so'}，可以画出字典树：  
![字典树](images/字典树.png)  
代码：[字典树实现代码](字典树(Trie)/实现字典树.py)  
Python版本的代码借鉴了两个版本:  
版本一：[代码](https://github.com/BlossomingL/leetcode/blob/master/%E5%AD%97%E5%85%B8%E6%A0%91(Trie)/%E5%AE%9E%E7%8E%B0%20Trie%20(%E5%89%8D%E7%BC%80%E6%A0%91)%E7%89%88%E6%9C%AC1.py)  
版本二：[代码](https://github.com/BlossomingL/leetcode/blob/master/%E5%AD%97%E5%85%B8%E6%A0%91(Trie)/%E5%AE%9E%E7%8E%B0%20Trie%20(%E5%89%8D%E7%BC%80%E6%A0%91)%E7%89%88%E6%9C%AC2.py)  
这两个版本的唯一不同的就是定义存储字典树的数据结构稍微有点差别，前者仅仅使用一个字典以及是否为最后一个单词的标记，后者为每个单词设置一个对象，对象中包含下一个单词和是否为最后一个单词。有时候后面一个版本可能会方便一点。  
leetcode相关题目：[实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/), [添加与搜索单词 - 数据结构设计](https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/), [单词替换](https://leetcode-cn.com/problems/replace-words/)

***
## 回溯算法

解决回溯问题最好的方法就是先将树形图画出来，举个例子对于简单的全排列问题，即求集合｛1,2,3｝的全排列。画出树形图如下：
![全排列](images/全排列.png)
