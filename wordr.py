#read wordlist
#نها تقوم بأخذ قائمة من النصوص وتقوم بتشفيرهم حسب ما تريد

class wordlist_read: #قمنا بعمل كلاس لتقوم بقرائة قائمة النصوص
	def list_read(self,word_list):
		file = open(word_list, "r")
		return  file.readlines() #لاجل اعادة عند الاستدعاء	
