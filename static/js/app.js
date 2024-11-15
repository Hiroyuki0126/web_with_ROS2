// app.js
function startArrangement() {
  const numberOfPeople = document.getElementById('numberOfPeople').value;
  const arrangementPattern = document.querySelector('input[name="arrangementPattern"]:checked');

  if (!numberOfPeople || !arrangementPattern) {
    alert("人数と配置パターンを選択してください。");
    return;
  }

  const data = {
    numberOfPeople: numberOfPeople,
    pattern: arrangementPattern.value
  };

  fetch('/api/send_command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log("開始データ:", data);
        alert("配置が開始されました！");
    })
    .catch((error) => {
        console.error('エラー:', error);
        alert('送信に失敗しました。');
    });
}

function stopArrangement() {
  console.log("配置作業を中断しました。");
  alert("配置作業が中断されました。");
  // ここにロボットへの中断API送信処理を追加
}