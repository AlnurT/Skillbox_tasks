"""Задача 10. Истина

К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python.
Напишите программу, которая реализует алгоритм дешифровки этого текста.
Расшифруйте текст с помощью своей программы, а затем найдите его в интернете.

vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf
jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp
djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme
wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv
Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc
bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ
ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf
b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip

Подсказка
В задаче говорится об истине питона import this, а текст зашифрован шифром Цезаря.
"""


cipher = (
    "vujgvmCfb tj ufscfu ouib z/vhm "
    "jdjuFyqm jt fscfuu uibo jdju/jnqm "
    "fTjnqm tj scfuuf ibou fy/dpnqm "
    "yDpnqmf jt cfuufs boui dbufe/dpnqmj "
    "uGmb tj fuufsc ouib oftufe/ "
    "bstfTq jt uufscf uibo otf/ef "
    "uzSfbebcjmj vout/dp "
    "djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf "
    "ipvhiBmu zqsbdujdbmju fbutc uz/qvsj "
    "Fsspst tipvme wfsof qbtt foumz/tjm "
    "omfttV mjdjumzfyq odfe/tjmf "
    "Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv "
    "Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ "
    "Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud "
    "xOp tj scfuuf ibou /ofwfs "
    "uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op "
    "gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb "
    "Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ "
    'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
)


def decipher_with_caesar_cipher(cipher: str, caesar_shift: int) -> list:
    caesar_cipher = ""
    for symbol in cipher:
        if symbol != " ":
            symbol = chr(ord(symbol) + caesar_shift)
        caesar_cipher = f"{caesar_cipher}{symbol}"
    return caesar_cipher.split()


def shift_character_position(caesar_cipher_list: list, symbol_shift: int) -> list:
    philosophy_text_list = []
    for word in caesar_cipher_list:
        word_length = len(word)
        if abs(symbol_shift) > word_length:
            new_shift = -(abs(symbol_shift) % word_length)
        else:
            new_shift = symbol_shift
        word = f"{word[new_shift:]}{word[-word_length:new_shift]}"
        philosophy_text_list.append(word)
        if "." in word:
            symbol_shift -= 1
    return philosophy_text_list


def main():
    caesar_shift = -1
    caesar_cipher_list = decipher_with_caesar_cipher(cipher, caesar_shift)

    symbol_shift = -3
    philosophy_text_list = shift_character_position(caesar_cipher_list, symbol_shift)

    philosophy_text = " ".join(philosophy_text_list)
    philosophy_text = ".\n".join(philosophy_text.split(". "))

    print(f"Текст философии программирования: \n{philosophy_text}")


if __name__ == "__main__":
    main()
