AULA 2 - 11/03 TERÇA-FEIRA

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
              'Perfil de Usuário',
              style: TextStyle(
                  color: Color(0xffffffff), fontWeight: FontWeight.bold),
            ),
            backgroundColor: Color(0xffcb93ff),
          ),
          body: Container(
            width: double.infinity,
            height: double.infinity,
            color: Color(0xffffffff),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Image.asset(
                  'img/cat-icon.png',
                  height: 150.0,
                  width: 150.0,
                ),
                SizedBox(width: 20, height: 20),
                Text(
                  'Nome: João Silva',
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                    color: Color(0xffcb93ff),
                  ),
                ),
                Text(
                  'Idade: 20 anos',
                  style: TextStyle(fontSize: 20, color: Color(0xff7a7a7a)),
                ),
                Text(
                  'Cidade: Campo Grande',
                  style: TextStyle(fontSize: 18, color: Color(0xff7a7a7a)),
                ),
                ElevatedButton(onPressed: onPressed, child: child)
              ],
            ),
          ),
        ));
  }
}
