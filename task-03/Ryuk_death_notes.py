#Ryuk and His Death Notes :

diff_papers=int(input())
paper_req=input()
paper_ava=input()

def death_notes(paper_ava,paper_req,diff_papers):
    for i in range(diff_papers):
      if (int(paper_ava[i])-int(paper_req[i])<int(paper_req[i])):
       return 1
      if (int(paper_ava[i])-int(paper_req[i])>int(paper_req[i])):
       return 2
      else :
       return -1

print(death_notes(paper_ava,paper_req,diff_papers))
