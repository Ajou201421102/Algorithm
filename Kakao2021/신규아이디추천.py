def solution(new_id):
    answer = ''
    answer = phase1(new_id)

    answer = phase2(answer)

    answer = phase3(answer)

    answer = phase4(answer)
    print(answer)
    answer = phase6(answer)
    print(answer)
    answer = phase7(answer)
    print(answer)
    return answer


def phase1(new_id):
    result = ""
    for word in new_id:
        if word.isalpha():
            word = word.lower()
        result += word
    return result


def phase2(new_id):
    result = ""
    for word in new_id:
        if word.isalpha() or word.isdigit() or word == "-" or word == "_" or word == ".":
            result += word
    return result


def phase3(new_id):
    result = ""
    check = True
    for i in range(0,len(new_id)):
        #print(word)
        if new_id[i] == ".":
            if check:
                result += "."
                check = False
            else:
                i += 1                      
        else:
            result += new_id[i]
            check = True
    return result


def phase4(new_id):
    result = ""
    temp = ""
#     if new_id.startswith("."):
#         result = ""
#         check = False
#         for word in new_id:
#             if word == "." and check:
#                 result += word
#             elif word =="." and not check:
#                 check = False
#             else:
#                 result +=word
#                 check = True
#     if result.endswith("."):
#         check = 0
#         temp = ""
#         for i in range(len(result)-1,0,-1):
#             if new_id[i] != ".":
#                 check = i
#                 break
        
#         for i in range(0,check+1):
#             temp += result[i]
#         result = temp
    for word in new_id:
        if word == ".":
            temp += " "
        else:
            temp += word
    temp = temp.strip()
    for word in temp:
        if word == " ":
            result += "."
        else:
            result += word
    if result == "":
        result = "a"
    return result


def phase6(new_id):
    result = ""
    if len(new_id)>=16:
        for i in range(0,15):
            result += new_id[i]
        result = phase4(result)
    else:
        result = new_id
    return result

def phase7(new_id):
    temp = new_id
    result = ""
    if len(new_id)<=2:
        while(len(temp)<3):
            temp += new_id[len(new_id)-1]
        print(temp)
        for i in range(0,3):
            result += temp[i]
        print("result : ",result)
    else:
        result = new_id
        
    return result