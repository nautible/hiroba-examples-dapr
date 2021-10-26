# service-invocation

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
