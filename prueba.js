function fibonacciGenerator(n) {
    var datos = [];
    if (n === 1){
        datos =[0];
    }
    else if (n === 2){
        datos = [0,1];
    }
    else {
    datos = [0,1];
    for (var inicio=2; inicio < n; inicio++){
        datos.push(datos[datos.length-1 ]+ datos[datos.length -2])
    }
}
    return datos;   
}

var resultado = fibonacciGenerator(10)
console.log(resultado)