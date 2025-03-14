// AULA 1 - 10/03 SEGUNDA-FEIRA

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  // Este widget é a raiz do seu aplicativo.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text(
            'Perfil do Usuário',
            style: TextStyle(color: Colors.pink, fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.yellow,
        ),
        body: Container(
          width: double.infinity,
          height: double.infinity,
          color: Colors.black,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Nome: João Silva',
                style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue,
                ),
              ),
              SizedBox(width: 15),
              Text(
                'Idade: 20 anos',
                style: TextStyle(
                  fontSize: 20,
                  color: Colors.red,
                  fontStyle: FontStyle.italic,
                ),
              ),
              Text(
                'Cidade: Campo Grande',
                style: TextStyle(fontSize: 18, color: Colors.purple),
              ),
              Text(
                'Nome: Maria Oliveira',
                style: TextStyle(
                  fontSize: 30,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue,
                ),
              ),
              SizedBox(width: 15),
              Text(
                'Idade: 25 anos',
                style: TextStyle(
                  fontSize: 20,
                  color: Colors.red,
                  fontStyle: FontStyle.italic,
                ),
              ),
              Text(
                'Cidade: São Paulo',
                style: TextStyle(fontSize: 18, color: Colors.purple),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
