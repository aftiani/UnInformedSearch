#BFS
#pertama = B
#tujuan = H
#jalur

#DFS
#pertama1 = B
#tujuan2 = H
#jalur2

JNE =  {'A':set(['B']),
         'B':set(['C','A','D','F']),
         'C':set(['B']),
         'D':set(['B','E']),
         'E':set(['D','F','H']),
         'F':set(['B','E','G']),
         'G':set(['F','H']),
         'H':set(['E','G'])}


def bfs(graf, pertama, akhir):
    queue = [[pertama]]
    visited = set()

    while queue:

        jalur = queue.pop(0)


        state = jalur[-1]


        if state == akhir:
            return jalur

        elif state not in visited:

            for cabang in graf.get(state, []):
                jalur_baru = list(jalur)
                jalur_baru.append(cabang)
                queue.append(jalur_baru)


            visited.add(state)

            isi = len(queue)
            if isi == 0:
                print("Tidak ditemukan")

def dfs(graf2, pertama1,akhir1):
    stack = [[pertama1]]
    visited2 = set()

    while stack:

            jalur2 = stack.pop(-1) # ambil data


            state2 = jalur2[-1]


            if state2 == akhir1:
                return jalur2

            elif state2 not in visited2:

                for cabang2 in graf2.get(state2, []):
                    jalur_baru2 = list(jalur2)
                    jalur_baru2.append(cabang2)
                    stack.append(jalur_baru2)

                visited2.add(state2)

            isi2 = len(stack)
            if isi2 == 0:
                print("Not Found")
print("Hasil dari BFS: ")
print(bfs(JNE,'B','H'))

print("Hasil dari DFS: ")
print(dfs(JNE,'B','H'))