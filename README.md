# ML204 Academic & Study Resources 📚

Welcome to the official study notes and resources repository for **ML204** — an interactive, mathematically rigorous machine learning curriculum.

This repository holds LaTeX derivations, compiled PDFs, lecture summaries, problem sets, and notebooks organized systematically by **Part / Chapter / Subchapter**.

🌐 **Interactive Web App**: [mlens-theta.vercel.app](https://mlens-theta.vercel.app)  
📱 **Android Offline Suite**: [Latest Release v1.0.1](https://github.com/ML204/ML204/releases)  
🏛️ **GitHub Organization**: [github.com/ML204](https://github.com/ML204)  

---

## 📂 Repository Structure

All resources follow the 3-tier hierarchy mirroring the core curriculum:
```text
<part-slug>/
  └── <chapter-slug>/
        └── <topic-slug>/
              ├── <Topic_Notes>.tex
              ├── <Topic_Notes>.pdf
              ├── <Topic_Summary>.md
              └── README.md
```

---

## 📑 Curriculum & Resource Index

### 📐 Part 1: Math Foundations


#### Linear Algebra

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Vectors and Matrices** | [`math-foundations/linear-algebra/vectors-and-matrices`](./math-foundations/linear-algebra/vectors-and-matrices) | `README.md`, `Vectors_and_Matrices_Summary.md` |
| **Dot Product and Matrix Multiplication** | [`math-foundations/linear-algebra/dot-product-matrix-multiply`](./math-foundations/linear-algebra/dot-product-matrix-multiply) | `README.md` |
| **Transpose, Inverse and Determinant** | [`math-foundations/linear-algebra/transpose-inverse-determinant`](./math-foundations/linear-algebra/transpose-inverse-determinant) | `README.md` |
| **Norms — L1 and L2** | [`math-foundations/linear-algebra/norms`](./math-foundations/linear-algebra/norms) | `README.md` |
| **Eigenvalues and Eigenvectors** | [`math-foundations/linear-algebra/eigenvalues-eigenvectors`](./math-foundations/linear-algebra/eigenvalues-eigenvectors) | `README.md` |
| **Singular Value Decomposition** | [`math-foundations/linear-algebra/svd`](./math-foundations/linear-algebra/svd) | `README.md` |

#### Calculus

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Derivatives and the Chain Rule** | [`math-foundations/calculus/derivatives-and-chain-rule`](./math-foundations/calculus/derivatives-and-chain-rule) | `README.md` |
| **Partial Derivatives** | [`math-foundations/calculus/partial-derivatives`](./math-foundations/calculus/partial-derivatives) | `README.md` |
| **Gradients and the Jacobian** | [`math-foundations/calculus/gradients-and-jacobian`](./math-foundations/calculus/gradients-and-jacobian) | `README.md` |
| **What is Optimization?** | [`math-foundations/calculus/what-is-optimization`](./math-foundations/calculus/what-is-optimization) | `README.md` |
| **Loss Functions** | [`math-foundations/calculus/loss-functions`](./math-foundations/calculus/loss-functions) | `README.md` |
| **Gradient Descent** | [`math-foundations/calculus/gradient-descent`](./math-foundations/calculus/gradient-descent) | `Gradient_Descent_Summary.md`, `README.md` |
| **Learning Rate and Convergence** | [`math-foundations/calculus/learning-rate`](./math-foundations/calculus/learning-rate) | `README.md` |
| **SGD vs Batch Gradient Descent** | [`math-foundations/calculus/sgd-vs-batch`](./math-foundations/calculus/sgd-vs-batch) | `README.md` |

#### Probability

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Random Variables and Distributions** | [`math-foundations/probability/random-variables-distributions`](./math-foundations/probability/random-variables-distributions) | `README.md` |
| **Expectation, Variance and Covariance** | [`math-foundations/probability/expectation-variance-covariance`](./math-foundations/probability/expectation-variance-covariance) | `README.md` |
| **Conditional Probability and Bayes' Rule** | [`math-foundations/probability/conditional-probability-bayes`](./math-foundations/probability/conditional-probability-bayes) | `README.md` |
| **Common Distributions** | [`math-foundations/probability/common-distributions`](./math-foundations/probability/common-distributions) | `README.md` |
| **Maximum Likelihood Estimation** | [`math-foundations/probability/maximum-likelihood-estimation`](./math-foundations/probability/maximum-likelihood-estimation) | `README.md` |

#### Statistics

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Sampling and the Central Limit Theorem** | [`math-foundations/statistics/sampling-and-clt`](./math-foundations/statistics/sampling-and-clt) | `README.md` |
| **Hypothesis Testing and p-values** | [`math-foundations/statistics/hypothesis-testing`](./math-foundations/statistics/hypothesis-testing) | `README.md` |
| **Confidence Intervals** | [`math-foundations/statistics/confidence-intervals`](./math-foundations/statistics/confidence-intervals) | `README.md` |
| **Correlation vs Causation** | [`math-foundations/statistics/correlation-vs-causation`](./math-foundations/statistics/correlation-vs-causation) | `README.md` |

#### Optimization and Information Theory

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **SGD, Momentum, RMSProp and Adam** | [`math-foundations/optimization-and-information-theory/sgd-momentum-adam`](./math-foundations/optimization-and-information-theory/sgd-momentum-adam) | `README.md` |
| **Convex vs Non-Convex Functions** | [`math-foundations/optimization-and-information-theory/convex-vs-nonconvex`](./math-foundations/optimization-and-information-theory/convex-vs-nonconvex) | `README.md` |
| **Entropy and Cross-Entropy** | [`math-foundations/optimization-and-information-theory/entropy-and-cross-entropy`](./math-foundations/optimization-and-information-theory/entropy-and-cross-entropy) | `README.md` |
| **KL Divergence** | [`math-foundations/optimization-and-information-theory/kl-divergence`](./math-foundations/optimization-and-information-theory/kl-divergence) | `README.md` |

### 🗄️ Part 2: Data Handling


#### Exploring Data

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Exploratory Data Analysis** | [`data-handling/exploring-data/eda`](./data-handling/exploring-data/eda) | `README.md` |
| **Summary Statistics and Distributions** | [`data-handling/exploring-data/summary-statistics`](./data-handling/exploring-data/summary-statistics) | `README.md` |
| **Correlation Analysis** | [`data-handling/exploring-data/correlation-analysis`](./data-handling/exploring-data/correlation-analysis) | `README.md` |

#### Cleaning

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Missing Values — Drop and Impute** | [`data-handling/cleaning/missing-values`](./data-handling/cleaning/missing-values) | `README.md` |
| **Outlier Detection and Treatment** | [`data-handling/cleaning/outlier-detection`](./data-handling/cleaning/outlier-detection) | `README.md` |
| **Duplicates and Inconsistent Labels** | [`data-handling/cleaning/duplicates-labels`](./data-handling/cleaning/duplicates-labels) | `README.md` |

#### Feature Work

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Scaling — Standardization and Min-Max** | [`data-handling/feature-work/scaling`](./data-handling/feature-work/scaling) | `README.md` |
| **Encoding — One-Hot, Label, Target** | [`data-handling/feature-work/encoding`](./data-handling/feature-work/encoding) | `README.md` |
| **Feature Engineering** | [`data-handling/feature-work/feature-engineering`](./data-handling/feature-work/feature-engineering) | `README.md` |
| **Feature Selection** | [`data-handling/feature-work/feature-selection`](./data-handling/feature-work/feature-selection) | `README.md` |
| **Dimensionality Reduction as Preprocessing** | [`data-handling/feature-work/dimensionality-reduction-prep`](./data-handling/feature-work/dimensionality-reduction-prep) | `README.md` |

#### Splitting and Pitfalls

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Train / Validation / Test Split** | [`data-handling/splitting-and-pitfalls/train-val-test-split`](./data-handling/splitting-and-pitfalls/train-val-test-split) | `README.md` |
| **Stratified Splits** | [`data-handling/splitting-and-pitfalls/stratified-splits`](./data-handling/splitting-and-pitfalls/stratified-splits) | `README.md` |
| **Time-Based Splits** | [`data-handling/splitting-and-pitfalls/time-based-splits`](./data-handling/splitting-and-pitfalls/time-based-splits) | `README.md` |
| **Data Leakage** | [`data-handling/splitting-and-pitfalls/data-leakage`](./data-handling/splitting-and-pitfalls/data-leakage) | `README.md` |
| **Class Imbalance** | [`data-handling/splitting-and-pitfalls/class-imbalance`](./data-handling/splitting-and-pitfalls/class-imbalance) | `README.md` |

### 📊 Part 3: Classical Machine Learning


#### Supervised — Regression

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Linear Regression** | [`classical-ml/supervised-regression/linear-regression`](./classical-ml/supervised-regression/linear-regression) | `Linear_Regression.pdf`, `Linear_Regression_Summary.md`, `README.md` |
| **Ordinary Least Squares (OLS)** | [`classical-ml/supervised-regression/ordinary-least-squares`](./classical-ml/supervised-regression/ordinary-least-squares) | `OLS.pdf`, `OLS_matrix_notes.tex`, `Ordinary_Least_Squares_Summary.md`, `README.md` |
| **Polynomial Regression** | [`classical-ml/supervised-regression/polynomial-regression`](./classical-ml/supervised-regression/polynomial-regression) | `Polynomial_Regression.pdf`, `Polynomial_Regression.tex`, `README.md` |
| **Ridge Regression** | [`classical-ml/supervised-regression/ridge-regression`](./classical-ml/supervised-regression/ridge-regression) | `README.md`, `Ridge_Regression_Notes.tex`, `Ridge_Regression_Summary.md`, `Ridge_regression.pdf` |
| **Lasso Regression** | [`classical-ml/supervised-regression/lasso-regression`](./classical-ml/supervised-regression/lasso-regression) | `Lasso_Regression.pdf`, `Lasso_Regression_Notes.tex`, `Lasso_Regression_Summary.md`, `README.md` |

#### Supervised — Classification

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Logistic Regression** | [`classical-ml/supervised-classification/logistic-regression`](./classical-ml/supervised-classification/logistic-regression) | `README.md` |
| **k-Nearest Neighbors** | [`classical-ml/supervised-classification/knn`](./classical-ml/supervised-classification/knn) | `README.md` |
| **Naive Bayes** | [`classical-ml/supervised-classification/naive-bayes`](./classical-ml/supervised-classification/naive-bayes) | `README.md` |
| **Support Vector Machines and Kernels** | [`classical-ml/supervised-classification/svm-and-kernels`](./classical-ml/supervised-classification/svm-and-kernels) | `README.md` |
| **Decision Trees** | [`classical-ml/supervised-classification/decision-trees`](./classical-ml/supervised-classification/decision-trees) | `README.md` |

#### Ensemble Methods

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Bagging and Random Forests** | [`classical-ml/ensemble-methods/bagging-and-random-forests`](./classical-ml/ensemble-methods/bagging-and-random-forests) | `README.md` |
| **Gradient Boosting** | [`classical-ml/ensemble-methods/gradient-boosting`](./classical-ml/ensemble-methods/gradient-boosting) | `README.md` |
| **XGBoost and LightGBM** | [`classical-ml/ensemble-methods/xgboost-lightgbm`](./classical-ml/ensemble-methods/xgboost-lightgbm) | `README.md` |
| **Stacking and Voting** | [`classical-ml/ensemble-methods/stacking-and-voting`](./classical-ml/ensemble-methods/stacking-and-voting) | `README.md` |

#### Unsupervised Learning

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **k-Means Clustering** | [`classical-ml/unsupervised-learning/kmeans`](./classical-ml/unsupervised-learning/kmeans) | `README.md` |
| **Hierarchical Clustering** | [`classical-ml/unsupervised-learning/hierarchical-clustering`](./classical-ml/unsupervised-learning/hierarchical-clustering) | `README.md` |
| **DBSCAN** | [`classical-ml/unsupervised-learning/dbscan`](./classical-ml/unsupervised-learning/dbscan) | `README.md` |
| **Gaussian Mixture Models** | [`classical-ml/unsupervised-learning/gaussian-mixture-models`](./classical-ml/unsupervised-learning/gaussian-mixture-models) | `README.md` |
| **PCA** | [`classical-ml/unsupervised-learning/pca`](./classical-ml/unsupervised-learning/pca) | `README.md` |
| **t-SNE and UMAP** | [`classical-ml/unsupervised-learning/tsne-umap`](./classical-ml/unsupervised-learning/tsne-umap) | `README.md` |

#### Anomaly Detection

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Statistical Thresholds** | [`classical-ml/anomaly-detection/statistical-thresholds`](./classical-ml/anomaly-detection/statistical-thresholds) | `README.md` |
| **Isolation Forest** | [`classical-ml/anomaly-detection/isolation-forest`](./classical-ml/anomaly-detection/isolation-forest) | `README.md` |
| **One-Class SVM** | [`classical-ml/anomaly-detection/one-class-svm`](./classical-ml/anomaly-detection/one-class-svm) | `README.md` |
| **Autoencoder-Based Detection** | [`classical-ml/anomaly-detection/autoencoder-detection`](./classical-ml/anomaly-detection/autoencoder-detection) | `README.md` |

#### Model Quality

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Overfitting, Underfitting and Bias-Variance** | [`classical-ml/model-quality/bias-variance-tradeoff`](./classical-ml/model-quality/bias-variance-tradeoff) | `README.md` |
| **L1 and L2 Regularization** | [`classical-ml/model-quality/l1-l2-regularization`](./classical-ml/model-quality/l1-l2-regularization) | `README.md` |
| **k-Fold Cross-Validation** | [`classical-ml/model-quality/cross-validation`](./classical-ml/model-quality/cross-validation) | `README.md` |
| **Grid Search and Random Search** | [`classical-ml/model-quality/grid-and-random-search`](./classical-ml/model-quality/grid-and-random-search) | `README.md` |
| **Metrics — Accuracy, Precision, Recall, F1** | [`classical-ml/model-quality/classification-metrics`](./classical-ml/model-quality/classification-metrics) | `README.md` |
| **ROC-AUC and PR Curve** | [`classical-ml/model-quality/roc-auc-pr`](./classical-ml/model-quality/roc-auc-pr) | `README.md` |
| **Metrics — RMSE, MAE, R-squared** | [`classical-ml/model-quality/regression-metrics`](./classical-ml/model-quality/regression-metrics) | `README.md` |
| **Confusion Matrix** | [`classical-ml/model-quality/confusion-matrix`](./classical-ml/model-quality/confusion-matrix) | `README.md` |

### 🧠 Part 4: Deep Learning


#### Neural Network Basics

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Perceptron and Multilayer Networks** | [`deep-learning/neural-network-basics/perceptron-and-mlp`](./deep-learning/neural-network-basics/perceptron-and-mlp) | `README.md` |
| **Activation Functions** | [`deep-learning/neural-network-basics/activation-functions`](./deep-learning/neural-network-basics/activation-functions) | `README.md` |
| **Loss Functions — MSE and Cross-Entropy** | [`deep-learning/neural-network-basics/loss-functions-dl`](./deep-learning/neural-network-basics/loss-functions-dl) | `README.md` |
| **Forward Pass and Backpropagation** | [`deep-learning/neural-network-basics/forward-pass-backprop`](./deep-learning/neural-network-basics/forward-pass-backprop) | `README.md` |
| **Weight Initialization** | [`deep-learning/neural-network-basics/weight-initialization`](./deep-learning/neural-network-basics/weight-initialization) | `README.md` |

#### Training Techniques

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Dropout** | [`deep-learning/training-techniques/dropout`](./deep-learning/training-techniques/dropout) | `README.md` |
| **Batch Normalization** | [`deep-learning/training-techniques/batch-normalization`](./deep-learning/training-techniques/batch-normalization) | `README.md` |
| **Learning Rate Schedules** | [`deep-learning/training-techniques/lr-schedules`](./deep-learning/training-techniques/lr-schedules) | `README.md` |
| **Early Stopping** | [`deep-learning/training-techniques/early-stopping`](./deep-learning/training-techniques/early-stopping) | `README.md` |
| **Data Augmentation** | [`deep-learning/training-techniques/data-augmentation`](./deep-learning/training-techniques/data-augmentation) | `README.md` |
| **Debugging a Model That Won't Learn** | [`deep-learning/training-techniques/debugging-a-model`](./deep-learning/training-techniques/debugging-a-model) | `README.md` |

#### Convolutional Networks

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Convolution, Pooling, Stride and Padding** | [`deep-learning/convolutional-networks/convolution-pooling`](./deep-learning/convolutional-networks/convolution-pooling) | `README.md` |
| **Classic Architectures — LeNet, VGG, ResNet** | [`deep-learning/convolutional-networks/classic-architectures`](./deep-learning/convolutional-networks/classic-architectures) | `README.md` |
| **Transfer Learning** | [`deep-learning/convolutional-networks/transfer-learning`](./deep-learning/convolutional-networks/transfer-learning) | `README.md` |

#### Sequence Models

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **RNN Basics and Vanishing Gradients** | [`deep-learning/sequence-models/rnn-and-vanishing-gradients`](./deep-learning/sequence-models/rnn-and-vanishing-gradients) | `README.md` |
| **LSTM and GRU** | [`deep-learning/sequence-models/lstm-and-gru`](./deep-learning/sequence-models/lstm-and-gru) | `README.md` |
| **Sequence-to-Sequence** | [`deep-learning/sequence-models/sequence-to-sequence`](./deep-learning/sequence-models/sequence-to-sequence) | `README.md` |

#### Attention and Transformers

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Self-Attention** | [`deep-learning/attention-and-transformers/self-attention`](./deep-learning/attention-and-transformers/self-attention) | `README.md` |
| **Transformer Architecture** | [`deep-learning/attention-and-transformers/transformer-architecture`](./deep-learning/attention-and-transformers/transformer-architecture) | `README.md` |
| **Positional Encoding** | [`deep-learning/attention-and-transformers/positional-encoding`](./deep-learning/attention-and-transformers/positional-encoding) | `README.md` |
| **BERT and GPT Overview** | [`deep-learning/attention-and-transformers/bert-and-gpt`](./deep-learning/attention-and-transformers/bert-and-gpt) | `README.md` |

#### Other Architectures

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Autoencoders** | [`deep-learning/other-architectures/autoencoders`](./deep-learning/other-architectures/autoencoders) | `README.md` |
| **Variational Autoencoders** | [`deep-learning/other-architectures/variational-autoencoders`](./deep-learning/other-architectures/variational-autoencoders) | `README.md` |
| **GANs Overview** | [`deep-learning/other-architectures/gans-overview`](./deep-learning/other-architectures/gans-overview) | `README.md` |

### 🔬 Part 5: Specialized Areas


#### Time Series and Sensor Data

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Trend, Seasonality and Stationarity** | [`specialized/time-series/trend-seasonality-stationarity`](./specialized/time-series/trend-seasonality-stationarity) | `README.md` |
| **Moving Averages and ARIMA** | [`specialized/time-series/moving-averages-arima`](./specialized/time-series/moving-averages-arima) | `README.md` |
| **Windowing Sensor Streams** | [`specialized/time-series/windowing-sensor-streams`](./specialized/time-series/windowing-sensor-streams) | `README.md` |
| **LSTM and 1D-CNN for Time Series** | [`specialized/time-series/lstm-cnn-time-series`](./specialized/time-series/lstm-cnn-time-series) | `README.md` |
| **Forecasting Evaluation** | [`specialized/time-series/forecasting-evaluation`](./specialized/time-series/forecasting-evaluation) | `README.md` |

#### Computer Vision

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Image Classification** | [`specialized/computer-vision/image-classification`](./specialized/computer-vision/image-classification) | `README.md` |
| **Object Detection — YOLO** | [`specialized/computer-vision/object-detection`](./specialized/computer-vision/object-detection) | `README.md` |
| **Segmentation Basics** | [`specialized/computer-vision/segmentation`](./specialized/computer-vision/segmentation) | `README.md` |

#### Natural Language Processing

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Tokenization** | [`specialized/nlp/tokenization`](./specialized/nlp/tokenization) | `README.md` |
| **Bag of Words and TF-IDF** | [`specialized/nlp/bag-of-words-tfidf`](./specialized/nlp/bag-of-words-tfidf) | `README.md` |
| **Word Embeddings** | [`specialized/nlp/word-embeddings`](./specialized/nlp/word-embeddings) | `README.md` |
| **Text Classification** | [`specialized/nlp/text-classification`](./specialized/nlp/text-classification) | `README.md` |
| **Fine-Tuning a Pretrained Model** | [`specialized/nlp/fine-tuning-pretrained`](./specialized/nlp/fine-tuning-pretrained) | `README.md` |

#### Large Language Models

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **How LLMs Are Trained** | [`specialized/large-language-models/how-llms-are-trained`](./specialized/large-language-models/how-llms-are-trained) | `README.md` |
| **Prompt Engineering** | [`specialized/large-language-models/prompt-engineering`](./specialized/large-language-models/prompt-engineering) | `README.md` |
| **Retrieval-Augmented Generation** | [`specialized/large-language-models/rag`](./specialized/large-language-models/rag) | `README.md` |
| **Fine-Tuning and LoRA** | [`specialized/large-language-models/fine-tuning-and-lora`](./specialized/large-language-models/fine-tuning-and-lora) | `README.md` |
| **Evaluating LLM Outputs** | [`specialized/large-language-models/evaluating-llm-outputs`](./specialized/large-language-models/evaluating-llm-outputs) | `README.md` |

#### Generative Models

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Diffusion Models Overview** | [`specialized/generative-models/diffusion-models`](./specialized/generative-models/diffusion-models) | `README.md` |
| **GANs vs VAEs vs Diffusion** | [`specialized/generative-models/gans-vs-vaes-vs-diffusion`](./specialized/generative-models/gans-vs-vaes-vs-diffusion) | `README.md` |

#### Reinforcement Learning

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Agents, Environments and Rewards** | [`specialized/reinforcement-learning/agents-environments-rewards`](./specialized/reinforcement-learning/agents-environments-rewards) | `README.md` |
| **Markov Decision Processes** | [`specialized/reinforcement-learning/markov-decision-processes`](./specialized/reinforcement-learning/markov-decision-processes) | `README.md` |
| **Q-Learning** | [`specialized/reinforcement-learning/q-learning`](./specialized/reinforcement-learning/q-learning) | `README.md` |
| **Policy Gradients Overview** | [`specialized/reinforcement-learning/policy-gradients`](./specialized/reinforcement-learning/policy-gradients) | `README.md` |

### 🚀 Part 6: MLOps and Deployment


#### Experiment Management

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Experiment Tracking — MLflow and W&B** | [`mlops/experiment-management/experiment-tracking`](./mlops/experiment-management/experiment-tracking) | `README.md` |
| **Dataset and Model Versioning** | [`mlops/experiment-management/dataset-model-versioning`](./mlops/experiment-management/dataset-model-versioning) | `README.md` |
| **Reproducibility** | [`mlops/experiment-management/reproducibility`](./mlops/experiment-management/reproducibility) | `README.md` |

#### Serving

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Wrapping a Model in an API** | [`mlops/serving/model-as-api`](./mlops/serving/model-as-api) | `README.md` |
| **Docker Basics** | [`mlops/serving/docker-basics`](./mlops/serving/docker-basics) | `README.md` |
| **Deploying to the Cloud** | [`mlops/serving/cloud-deployment`](./mlops/serving/cloud-deployment) | `README.md` |

#### Operations

| Topic | Folder Link | Available Files |
| :--- | :--- | :--- |
| **Model Monitoring** | [`mlops/operations/model-monitoring`](./mlops/operations/model-monitoring) | `README.md` |
| **Data Drift and Concept Drift** | [`mlops/operations/data-drift-concept-drift`](./mlops/operations/data-drift-concept-drift) | `README.md` |
| **Model Retraining Strategy** | [`mlops/operations/retraining-strategy`](./mlops/operations/retraining-strategy) | `README.md` |

---

## ✍️ How to Contribute Notes

We welcome contributions of mathematical derivations, concise summary sheets, Python code walk-throughs, and LaTeX notes.

1. **LaTeX Guidelines**:
   - Use standard AMS-LaTeX packages (`amsmath`, `amsfonts`, `amssymb`, `mathtools`).
   - Keep vector notation consistent: bold lowercase for vectors ($\\mathbf{w}$), bold uppercase for matrices ($\\mathbf{X}$).
   - Keep the corresponding compiled `.pdf` alongside the `.tex` source.
2. **Pull Requests**:
   - Locate the target `<part>/<chapter>/<topic>/` folder.
   - Add or update the notes.
   - Submit a Pull Request.

---

## 📜 License
Content in this repository is licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/) and accompanying code under the [MIT License](https://opensource.org/licenses/MIT).
