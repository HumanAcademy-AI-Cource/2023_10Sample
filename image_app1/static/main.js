const getImage = () => {
  axios
    // 画像を取得する
    .get("http://" + location.hostname + ":8080/get_image")
    // しばらくすると、取得した画像のパスがresponseに格納される
    .then((response) => {
      document.getElementById("imagebox").src = response.data;
    });
};
