from collections import Counter

def filecomparision(file1,file2):

    data1=[]
    with open(file1,'r') as f1:
        for line in f1:
            line = line.strip()
            data1.append(line)
        f1.close()
        data1 = list(filter(None, data1))

    freq_data1 = {e:k for e, k in Counter(data1).items() if k > 1}

    with open(file2,'r') as f2:
        data2 = []
        with open(file2, 'r') as f2:
            for line in f2:
                line = line.strip()
                data2.append(line)
            f2.close()
            data2 = list(filter(None, data2))

    freq_data2 = { e:k for e,k in Counter(data2).items() if k>1}



    result = {}

    similar_sentences = [each.strip() for each in list(set(data1)) if each in list(set(data2))]

    result['similar_sentences'] = similar_sentences

    result['similar_sentences_length'] = 'length : '+str(len(similar_sentences))

    data1_minus_data2 = [each.strip() for each in list(set(data1)) if each not in list(set(data2))]

    result['data1_minus_data2'] = data1_minus_data2

    result['data1_minus_data2_length'] = 'length : '+str(len(data1_minus_data2))

    #data2_minus_data1 = data2.difference(data1)

    data2_minus_data1 = [each.strip() for each in list(set(data2)) if each not in list(set(data1))]

    result['data2_minus_data1'] = data2_minus_data1

    result['data2_minus_data1_length'] = 'length : '+str(len(data2_minus_data1))

    result['freq_file_1'] = freq_data1

    result['freq_file_2'] = freq_data2

    return result




