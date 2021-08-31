import numpy as np
import math

dictionary_file = open("docs.txt","r")
query_file = open("queries.txt","r")
dictionary = {}
inverted_index = {}
document_angles = {}

dimension = len(set(dictionary_file.read().split()))
dictionary_file.seek(0)

document_no = 1
for document in dictionary_file:
    document_angles[document_no] = np.zeros(dimension)
    for word in document.split():
        if word not in dictionary.keys():
            dictionary[word] = len(dictionary)
        if word not in inverted_index.keys():
            inverted_index[word] = [document_no]
        elif document_no not in inverted_index[word]:
            inverted_index[word].append(document_no)
        document_angles[document_no][dictionary[word]] += 1
    document_no += 1

print(f"Words in dictionary:  {len(dictionary)}")

for query in query_file:
    print(f"Query:  {query.rstrip()}")
    results = []
    for word in query.split():
        if word in inverted_index.keys():
            results.append(inverted_index[word])
    
    if len(results) != 0 or len(results) == 1:
        relevant_documents = set(results[0])
        for result in results[1:]:
            relevant_documents &= set(result)
    else:
        relevant_documents = None
        
    print(f"Relevant documents: ",end="")
    for document_id in relevant_documents:
        print(f"{document_id} ",end="")
    print()

    query_vector = np.zeros(len(dictionary))
    
    for word in query.split():
        query_vector[dictionary[word]] = 1

    angles = {}
    for document_id in relevant_documents:
        angles[document_id] = math.degrees(math.acos(query_vector.dot(document_angles[document_id])/(np.linalg.norm(query_vector)*np.linalg.norm(document_angles[document_id]))))

    sorted_angles = sorted(relevant_documents,key=angles.__getitem__)

    for document_id in sorted_angles:
        print(f"{document_id} {angles[document_id]:.5f}")