# publish / subscribe （宣言的手法）

サンプルコードをminikubeおよびAWSで確認するための手順です。

## 環境の前提条件
- [dockerのインストール](https://docs.docker.jp/desktop/index.html#desktop-download-and-install)
- [minikubeのインストール](https://kubernetes.io/docs/tasks/tools/)
- [Skaffoldのインストール](https://skaffold.dev/docs/install/)
- [Daprのインストール](https://docs.dapr.io/operations/hosting/kubernetes/kubernetes-deploy/)

## ビルド＆デプロイ（minikube）

skaffoldを使い、minikubeにデプロイします

- NATS

```
kubectl apply -f https://raw.githubusercontent.com/nats-io/k8s/master/nats-server/single-server-nats.yml
kubectl apply -f https://raw.githubusercontent.com/nats-io/k8s/master/nats-streaming-server/single-server-stan.yml
```

- Daprコンポーネント

```
kubectl apply -f deploy/minikube/
```

- orderアプリケーション

```
cd order
skaffold dev --port-forward
```

- paymentアプリケーション

```
cd payment
skaffold dev
```

- stockアプリケーション

```
cd stock
skaffold dev
```

## ビルド（AWS向け）

AWS ECRへのアップロードについて詳細な手順は[公式ドキュメント](https://docs.aws.amazon.com/ja_jp/AmazonECR/latest/userguide/getting-started-cli.html)を参照

```
cd order
docker build -t <account-id>.dkr.ecr.<region>.amazonaws.com/order-image:latest .
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/order-image:latest
```

## デプロイ（AWS）

- コードの修正

deploy/application配下のorder.yaml,payment.yaml,subscribe.yaml
```
+      - image: <account-id>.dkr.ecr.<region>.amazonaws.com/order-image:latest # for ECR
-      - image: order-image
```

- Daprコンポーネント

```
k apply -f deploy/aws/
```

- アプリケーション

```
kubectl apply -f deploy/application/
```
