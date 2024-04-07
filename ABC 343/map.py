var move = {
      "name": "だいもんじ",
    "damage": 110,
    "accuracy": 85
  }// こんなオブジェクトを作ってみる
var properties = ["damage","accuracy"];// mapを使う配列はこっち
properties.map(function(value){ // アロー関数「ではない」ことに注意
    console.log(this[value])
}, move )// 第二引数にオブジェクトmoveを設定
