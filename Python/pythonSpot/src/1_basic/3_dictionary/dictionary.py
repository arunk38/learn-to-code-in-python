words = {"Hello": "Bonjour", "Yes": "Oui", "No": "Non", "Bye": "Au Revoir"}

print (words)         # print key-pairs.
del words["Yes"]       # delete a key-pair.
print (words)            # print key-pairs.
words["Yes"] = "Oui!"  # add new key-pair.
print (words)            # print key-pairs.

print(str(words.get('eggs',0)))
