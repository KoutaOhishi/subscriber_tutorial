#! /usr/bin/env python
# coding:utf-8
def decoder(input):
    """
        inputに暗号文を入れると、解読結果をreturnします。
    """
    import codecs
    return codecs.decode(str(input), "rot13")

#import xxxx


#if __name__ == "__main__":
