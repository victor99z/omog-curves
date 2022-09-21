# Trabalho 01 - Modelagem geometrica

> Parte 1: Bezier grau 5 (6 control points)

> Parte 2: B-Spline Grau 4 (Uniforme com repetição no início e fim do vetor de nós) 
> + continuacao C0 das duas curvas

### Para executar:

``` 
$ python3 main.py
```

> use a tecla `b` para realizar a junçao em c0

### Libs/Langs necessarias:
- Pygame
- Python3.8

### Links uteis:

`Bezier`

- https://www.youtube.com/watch?v=YATikPP2q70
- https://www.youtube.com/watch?v=-aiErrvLRfE
- https://www.youtube.com/watch?v=pnYccz1Ha34
- [Algoritmo de Casteljau](https://pt.wikipedia.org/wiki/Algoritmo_de_De_Casteljau)
- https://splines.readthedocs.io/en/latest/euclidean/bezier-de-casteljau.html

`B-Spline`

- https://math.stackexchange.com/questions/2817170/what-is-the-purpose-of-having-repeated-knots-in-a-b-spline
- https://en.wikipedia.org/wiki/De_Boor%27s_algorithm
- https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html
- https://tiborstanko.sk/teaching/geo-num-2016/tp3.html
- http://nurbscalculator.in/

- Knots = degree + len(control_points) + 1
  - Repeticao nos knots = len(degree + 1) no inicio e no final
    - sendo 4 o degree {0,0,0,0,0, .... , 1,1,1,1,1}


### TODO:

- [x] Junção em usando continuidade C0
- [x] Junção em usando continuidade ~~C1~~ G1
- [ ] Junção em usando continuidade ~~C2~~ G2
