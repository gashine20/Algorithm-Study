SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
where I.SEX_UPON_INTAKE LIKE 'Intact%' and
(O.SEX_UPON_OUTCOME LIKE 'Neutered%' or O.SEX_UPON_OUTCOME LIKE 'Spayed%')
ORDER BY I.ANIMAL_ID ASC