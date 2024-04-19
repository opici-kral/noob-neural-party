import hashlib as h


def dictionary_builder(file: str) -> list[str]:
    vocabulary = set()
    for i in range(0, len(file)):
        if file[i] in [" ", ".", ",", "\n"]:
            j = i+1
            word = ""
            if len(file) - 10 < j:
                break
            while file[j] not in [" ", ".", ",", "\n"]:
                word += file[j]
                j += 1
            vocabulary.add(word.lower())
    return vocabulary


def check_my_hash(crack_str: str, tokens: list[str], algorithm: str):
    if algorithm == "md5":
        for token in tokens:
            token_md5 = h.md5(bytes(token, encoding='utf-8'))
            if token_md5.hexdigest() == crack_str:
                print(token)
    elif algorithm == "sha":
        for token in tokens:
            token = token
            token_sha1 = h.sha1(bytes(token, encoding='utf-8'))
            token_sha256 = h.sha256(bytes(token, encoding='utf-8'))
            token_sha384 = h.sha384(bytes(token, encoding='utf-8'))
            token_sha224 = h.sha3_224(bytes(token, encoding='utf-8'))
            token_sha2247 = h.sha224(bytes(token, encoding='utf-8'))
            token_sha2566 = h.sha3_256(bytes(token, encoding='utf-8'))
            token_sha512 = h.sha512(bytes(token, encoding='utf-8'))
            token_sha333 = h.sha3_384(bytes(token, encoding='utf-8'))
            token_sha33d = h.sha3_512(bytes(token, encoding='utf-8'))

            encrypted_tokens = [token_sha1, token_sha256, token_sha384, token_sha224, token_sha2247, token_sha2566, token_sha512, token_sha333, token_sha33d]
            for encrypted_token in encrypted_tokens:
                #print(encrypted_token.hexdigest().upper())
                if crack_str in encrypted_token.hexdigest().upper():
                    print(token)


f_cain = open("cain.txt", encoding="utf-8")
f_cain_str = f_cain.read()
tokens = list(dictionary_builder(f_cain_str))
check_my_hash("CBFDAC6008F9CAB4083784CBD1874F76618D2A97", tokens, "sha")

