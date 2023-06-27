function getText() {
  axios
    // テキストを取得する
    .get("http://" + location.hostname + ":8080/get_text")

    // しばらくすると、取得したテキストがresponseに格納される
    .then((response) => {
      // textboxというIDの要素にテキストを入れる
      document.getElementById("textbox").innerText = response.data;
    });
}
