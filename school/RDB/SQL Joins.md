```sql
SELECT column1, A2.column2 FROM A 
	JOIN B ON A.tabela = B.tabela // Will show A then B
	JOIN B AS A2 ON B.tabela = A2.tabela	
```