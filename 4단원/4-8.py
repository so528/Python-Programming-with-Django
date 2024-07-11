inlines = [ChoiceInline]  
list_display = ('question_text', 'pub_date')  
list_filter = ['pub_date']  
search_fields = ['question_text']  
