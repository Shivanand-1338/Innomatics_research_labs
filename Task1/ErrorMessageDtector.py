logs=["INFO","ERROR","WARNING","ERROR"]

error_count=0
for log in logs:
    if log=="ERROR":
        error_count+=1
print("Number of Error Logs:",error_count)