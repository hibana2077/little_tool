#Use MIT License
from chia.util.ints import uint32
from chia.util.bech32m import encode_puzzle_hash
from chia.util.keychain import mnemonic_to_seed
from chia.consensus.coinbase import create_puzzlehash_for_pk
from chia.wallet.derive_keys import master_sk_to_farmer_sk,master_sk_to_wallet_sk,master_sk_to_wallet_sk_unhardened
from blspy import AugSchemeMPL
import inquirer
import datetime
import os


coin_list = ["Chia", "Flax", "Flora", "HDD", "STAI", "Stor", "AedgeCoin", "Apple", "Avocado", "Beer", "Beet", "BTCgreen", "C*ntCoin", "Cactus",
             "Cannabis", "Chaingreen", "Covid", "CryptoDoge", "DogeChia", "Equality", "ETHgreen", "Fork", "Goji", "Goldcoin", "GreenDoge", "Kale",
             "Kiwi", "Kujenga", "LittleLamboCoin", "Lotus", "Lucky", "Maize", "Melati", "mELON", "Mint", "Mogua", "N-Chain", "Olive", "Peas", "PecanRolls",
             "Pipscoin", "Rose", "Salvia", "Scam", "Sector", "Seno", "SHIBgreen", "Skynet", "Socks", "Spare", "Taco", "Tad", "Thyme", "Tranzact", "Venidium",
             "Wheat", "Xcha", "Achi", "Silicoin", "Gold", "Profit", "Ecostake"]

prefix_list = ["xch", "xfx", "xfl", "hdd", "stai", "stor", "aec", "apple", "avo", "xbr", "xbt", "xbtc", "vag", "cac",
               "cans", "cgn", "cov", "xcd", "xdg", "xeq", "xeth", "xfk", "xgj", "ozt", "gdog", "xka",
               "xkw", "xkj", "llc", "lch", "six", "xmz", "xmx", "melon", "xkm", "mga", "nch", "xol", "pea", "rolls",
               "pips", "xcr", "xslv", "scm", "xsc", "xse", "xshib", "xnt", "sock", "spare", "xtx", "tad", "xth", "trz", "xvm",
               "wheat", "xca", "ach", "sit", "gl", "profit", "eco"]



def get_address(mnemonic):

  
    blockchain = [inquirer.List('blockchains', message="Blockchain", choices=coin_list,), ]
    fork = inquirer.prompt(blockchain)['blockchains']

    for prefix, name in zip(prefix_list, coin_list):
        if name == fork:

            seed = mnemonic_to_seed(mnemonic)
            key = AugSchemeMPL.key_gen(seed)
            fingerprint = (key.get_g1().get_fingerprint())
            mpk = (key.get_g1())
            fpk = (master_sk_to_farmer_sk(key).get_g1())
            puzhash = (create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(0)).get_g1()))

            with open('getaddress.txt', 'a') as file:
                print(f"User : {os.getlogin()}")
                print("\n" + "Master Public Key:", mpk)
                print("Farmer Public Key:", fpk)
                print("Fingerprint:", fingerprint)
                print("Puzzle Hash:", puzhash)
                print("\n" + "Master Mnemonic: " + mnemonic + "\n")

                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write(f"{time:=^50}" + "\n")
                file.write("\n\n" + "Master Public Key:" + str(mpk))
                file.write("\n" + "Farmer Public Key:" + str(fpk))
                file.write("\n" + "Fingerprint:" + str(fingerprint))
                file.write("\n" + "Puzzle Hash:" + str(puzhash))
                file.write("\n\n" + "Master Mnemonic: " + mnemonic + "\n")
                #
                Observer_address_list = [encode_puzzle_hash(create_puzzlehash_for_pk(master_sk_to_wallet_sk_unhardened(key, uint32(t)).get_g1()), prefix) for t in range(10)]
                Non_Observer_address_list = [encode_puzzle_hash(create_puzzlehash_for_pk(master_sk_to_wallet_sk(key, uint32(t)).get_g1()), prefix) for t in range(10)]
                #
                print("Observer address list: ")
                print("\n".join(Observer_address_list))
                print("\n" + "Non Observer address list: ")
                print("\n".join(Non_Observer_address_list))
                #
                file.write("Observer address list: " + "\n")
                file.write("\n".join(Observer_address_list))
                file.write("\n" + "Non Observer address list: " + "\n")
                file.write("\n".join(Non_Observer_address_list))
                file.write("\n\n" + f"{os.getlogin():=^50}"+ "\n\n")
            file.close()

if __name__ == '__main__':
    mnemonic = input("Please enter your mnemonic: ")
    get_address(mnemonic)
    print("Done! check getaddress.txt")