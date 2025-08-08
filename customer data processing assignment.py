customer_name = " JANE DOE "
clean_name=customer_name.strip()
print(clean_name)
lowercase_name=clean_name.lower()
print(lowercase_name)
titlecase_name=lowercase_name.title()
print(titlecase_name)
book_title="the little prince"
formatted_title=book_title.capitalize()
print(formatted_title)
product_code= "bk-457-nOVEL"
uppercase_code=product_code.upper()
print(uppercase_code)
new_seperator_code=uppercase_code.replace("-","/")
print(new_seperator_code)
review="This book is great.I love this book"
book_count=print(review.count("book"))
serial_number="987654321"
print(serial_number.isdigit())
url_parts=["the","book","nook","online"]
url_string="-".join(url_parts[::1])
print(url_string)
sentence_string=url_string.replace("-"," ") 
print(sentence_string)
offer_code='FRESHIPPING'
offer_code_uppercase=offer_code.isupper()
print(offer_code_uppercase)
feedback_message_length="I am very happy with my order"
message_length=len(feedback_message_length)
print(message_length)