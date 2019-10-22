MESSAGE := "Hello"
hello:doit
	@echo $(MESSAGE)
fuck:
	@echo fuck


task-a:
	@touch a.txt
	@make task-b
task-b:a.txt
	@echo u
	@touch b.txt
	@make task-c
task-c:b.txt
	@echo bitch
	@rm *.txt

doit:fuck
	@make task-a

train:prepare_data
	@echo fight!

prepare_data:
	@echo lets
