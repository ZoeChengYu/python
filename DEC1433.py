def inppt():
    strs=input()
    wd=strs.split('-')
    return strs,wd

def Violationword(keyword):
    banword={'FOP','FUC','FUG','FUQ','FUK','FUT','TMD','WTF','GPU','KGB','KKK','KMT','IQO','TIT','DPP','PRC','ROK','FTP','MKT','CPA','YSP','PDF','TSP','SDP','FHL','CCP','GPT','NPP','PFP','TSU','FBI','FOE','GOD','PUG','PUP','CAT','ANT','APE','FOX','HOG','PIG','PUG','DOG','BIG','MAD','NUN','SEX','NTR','SLY','BAD','GAY','ASD','BPH','ASS','BUM','BRA','CRY','LIE','SLY','SON','SOS','AGG','AGY','LGG','BAD','END','ERR','LAY','MAD','SED','FAT'}
    if len(keyword)!=3 or keyword in banword or any(c in keyword for c in "IO"):
        return True
    else:
        return False

def numsize(numword):
    if len(numword)!=4 or '4' in numword:
        return True
    else:
        return False

def main():
    strs,words=inppt()
    keyword=words[0]
    numword=words[1]
    if Violationword(keyword) or numsize(numword) or len(words)!=2:
        print(strs+' is Invalid license plate number.')
    else:
        print(strs+' is Valid license plate number.')

main()