# state-management

## 環境の前提条件
- [dockerのインストール](https://docs.docker.jp/desktop/index.html#desktop-download-and-install)
- [minikubeのインストール](https://kubernetes.io/docs/tasks/tools/)
- [Daprのインストール](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-deploy/)

## ビルド
- docker imageのビルド
```
docker build -t svc-c:1.0.0 svc-c
```

## デプロイ
- アプリケーションのデプロイ
```
kubectl apply -f deploy
```
- アプリケーションの削除
```
kubectl delete -f deploy
```
## 動作確認

- port-fowardでsvc-cのポート5000をローカルから実行できるようにする
```
kubectl port-forward svc/svc-c 5000:5000
```

- curlでsvc-cを実行しデータを保存する
```
curl -X POST -H "Content-Type: application/json" -d '{"product_id":"100", "quantity":"300"}'  localhost:5000/save
```

- curlでsvc-cを実行しデータを取得する
```
curl localhost:5000/get
```
