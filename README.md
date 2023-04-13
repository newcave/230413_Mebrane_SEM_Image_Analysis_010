# 230413_Mebrane_SEM_Image_Analysis_010


{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1DgEr_nhjYyQIPd71V8UMbbeQKjJSZBRr",
      "authorship_tag": "ABX9TyMlUilj7i1ZSEqlFAWh/HWX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "gpuClass": "standard"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/newcave/230413_Mebrane_SEM_Image_Analysis_010/blob/main/230413_Mebrane_SEM_Image_Analysis_101.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "4RNRxmK00YE4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "75bbc70b-f212-4cdf-a0b8-8fba4258a5a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pwd"
      ],
      "metadata": {
        "id": "gEiH-1Mm1MRF",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "46112228-7e5f-4ddb-ec56-74a4e6b89c40"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "64uKtoTQAA0c"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "# **3개의 threshold 값에 대해서 현재 까지 합친 버전**\n",
        "\n",
        "---\n",
        "\n"
      ],
      "metadata": {
        "id": "5pRwiBCAHLtt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#################### 3개의 threshold 값에 대해서 현재 까지 합친 버전 \n",
        "\n",
        "# from PIL import Image # 반전이미지 처리를 위한 ImageOps 추가 \n",
        "from PIL import Image, ImageOps\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# 검은색 농도의 임계값 리스트\n",
        "thresholds = [50, 60, 70, 80, 90, 100]\n",
        "#thresholds = [50, 60, 70, 80, 128, 150, 200, 250]\n",
        "#thresholds = [110, 128, 150]\n",
        "\n",
        "\n",
        "def main():\n",
        "    # 각 임계값에 대해 이미지 처리 및 출력\n",
        "    for threshold in thresholds:\n",
        "        process_images(threshold)\n",
