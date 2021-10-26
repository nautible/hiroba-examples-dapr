# service-invocation
サンプルコードをminkubeで動作確認するための手順です。

## 環境の前提条件
- [dockerのインストール](https://docs.docker.jp/desktop/index.html#desktop-download-and-install)
- [minikubeのインストール](https://kubernetes.io/docs/tasks/tools/)
- [Daprのインストール](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-deploy/)

## ビルド
- svc-aのdocker imageのビルド
```
docker build -t svc-a:1.0.0 svc-a
```
- svc-bのdocker imageのビルド
```
docker build -t svc-b:1.0.0 svc-b
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

- port-fowardでsvc-aのポート5000をローカルから実行できるようにする
```
kubectl port-forward svc/svc-a 5000:5000
```

- curlでsvc-aを実行して動作確認する
```
curl localhost:5000/api-api1
```
