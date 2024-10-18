def process_keyword(splited_sentence, pos_result):
    keyword = []
    # 키워드 배열 생성 위해 특정 부분 후처리
    for test_word in splited_sentence:
        temp_word = ''
        temp_word_arr = []
        temp_pos_arr = []
        while temp_word != test_word:
            pop_word, pop_pos = pos_result.pop(0)
            temp_word += pop_word
            temp_word_arr.append(pop_word)
            temp_pos_arr.append(pop_pos)

        result_words = []
        i = 0
        while i < len(temp_pos_arr):
            # josa 제외 any POS + Noun 패턴 결합
            if temp_pos_arr[i] != 'Josa' and i < len(temp_pos_arr) - 1 and temp_pos_arr[i + 1] == 'Noun':
                combined_word = temp_word_arr[i] + temp_word_arr[i + 1] 
                result_words.append(combined_word)
                # 결합 후 다음 인덱스로 넘어감
                i += 2  
            elif temp_pos_arr[i] == 'Noun' and i < len(temp_pos_arr) - 1 and temp_pos_arr[i + 1] != 'Josa':
                combined_word = temp_word_arr[i] + temp_word_arr[i + 1] 
                result_words.append(combined_word)
                # 결합 후 다음 인덱스로 넘어감
                i += 2  
            # Noun + Any POS + Noun 패턴 결합
            elif i < len(temp_pos_arr) - 2 and temp_pos_arr[i] == 'Noun' and temp_pos_arr[i + 2] == 'Noun':
                # Noun, Unknown, Noun 결합
                combined_word = temp_word_arr[i] + temp_word_arr[i + 1] + temp_word_arr[i + 2] 
                result_words.append(combined_word)
                i += 3  # 결합 후 다음 인덱스로 넘어감
            # 붙어있는 Noun 결합
            elif temp_pos_arr[i] == 'Noun':
                combined_word = temp_word_arr[i]
                i += 1
                while i < len(temp_pos_arr) and temp_pos_arr[i] == 'Noun':
                    # 붙어있는 Noun 결합
                    combined_word += temp_word_arr[i]  
                    i += 1
                result_words.append(combined_word)
            # 그 외는 그냥 건너뛰기
            else:
                i += 1
        # keyword 배열 확장
        keyword.extend(result_words)

    return keyword
