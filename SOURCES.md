# 來源索引與查證方式

[← 回到第 18 章](chapters/18-maintainers-and-taiwan.md) · [回總目錄](README.md#閱讀目錄)

本書以計畫官方、上游專案文件、治理規則與企業自身工程說明為來源。下列日期是閱讀查核日，不是文章發布日。動態文件後續可能改動。

## 如何看待證據

- **官方目的**：支持主辦單位明確宣示的目標，不能直接證明目標已實現。
- **技術與治理文件**：支持目前描述的功能和角色；版本差異需另看正文。
- **企業案例**：支持該公司自述的使用或投入，不能推論整體市占或公司控制權。
- **本書分析**：從上述資料推導可能的影響，不冒充主辦方未公開的選題決策。

未取得逐項 Track 遴選紀錄、維護投入預算及所有企業貢獻占比，因此不為這些資訊填入推測數字。

## 01｜一個 AI 服務，為什麼需要這麼多基礎設施？

[閱讀本章](chapters/01-ai-service.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Welcome to vLLM](https://docs.vllm.ai/en/latest/) · vLLM | 推論與服務定位、Berkeley 起源、模型與硬體生態。；模型推論及服務、批次與記憶體管理能力；不引用自稱領先或效能倍數 | 2026-09-18 |
| [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/) · Kubernetes | 期望狀態、部署管理、自動恢復與可擴充介面的功能及限制。；部署、擴展、故障替換及平台功能邊界 | 2026-09-18 |
| [Introduction](https://datafusion.apache.org/user-guide/introduction.html) · Apache DataFusion | Rust、Arrow、可嵌入可擴充查詢引擎、規劃與運算能力、已知下游系統；可嵌入及延伸的查詢引擎，讓下游重用共同資料處理能力 | 2026-09-18 |

## 02｜程式碼公開以後，究竟是誰在管？

[閱讀本章](chapters/02-open-source-governance.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Governance Process](https://docs.vllm.ai/en/latest/governance/process/) · vLLM | Committer 身分屬個人、維護者責任與長期貢獻資格。；不同維護角色、個人貢獻與專案責任，以及治理權不出售 | 2026-09-18 |
| [The Open Source Definition](https://opensource.org/osd) · Open Source Initiative | 開源授權涉及原始碼、衍生修改及散布權利，不能等同治理權或無條件使用 | 2026-09-18 |
| [How the ASF works](https://www.apache.org/foundation/how-it-works/) · Apache Software Foundation | 基金會支援、PMC與個人治理角色的責任區分 | 2026-09-18 |
| [Contributing to the Apache Software Foundation](https://community.apache.org/contributors/) · Apache Software Foundation | 文件設計等非程式貢獻、持續品質與Committer邀請；各專案程序有差異 | 2026-09-18 |

## 03｜人人都能用，企業為什麼還要付錢維護？

[閱讀本章](chapters/03-why-companies-invest.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [The Open Source Definition](https://opensource.org/osd) · Open Source Initiative | 開源授權涉及原始碼、衍生修改及散布權利，不能等同治理權或無條件使用 | 2026-09-18 |
| [Why AWS loves Rust, and how we would like to help](https://aws.amazon.com/blogs/opensource/why-aws-loves-rust-and-how-wed-like-to-help/) · AWS | AWS於2020年自述因服務依賴Rust而聘用維護者、回饋社群與累積內部能力 | 2026-09-18 |
| [Confluent Cloud Overview](https://docs.confluent.io/cloud/current/get-started/confluent-cloud-basics.html) · Confluent | 商業服務提供部署升級支援及額外功能；不等同Apache Kafka本身 | 2026-09-18 |
| [Apache Project Independence](https://community.apache.org/projectIndependence.html) · Apache Software Foundation | 企業雇用與贊助不自動換得治理權；專案依PMC共識治理 | 2026-09-18 |

## 04｜TAIONE 希望台灣的角色發生什麼改變？

[閱讀本章](chapters/04-taione-intent.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Apache Project Independence](https://community.apache.org/projectIndependence.html) · Apache Software Foundation | 企業雇用與贊助不自動換得治理權；專案依PMC共識治理 | 2026-09-18 |
| [TAIONE 基金會簡介](https://taione.org/about/intro) · 財團法人開源基金會 TAIONE | 人才、國際Committer與治理角色、技術自主與產業連結的官方目的 | 2026-09-18 |
| [TAIONE Fellowship 計畫介紹](https://taione.org/fellowship/about) · 財團法人開源基金會 TAIONE | 計畫意圖、Track Lead帶領、Code Review與架構討論、上游成果紀錄 | 2026-09-18 |
| [TAIONE 計畫與業務](https://taione.org/programs) · 財團法人開源基金會 TAIONE | 核心貢獻者培育與硬體、資服、國際合作及市場機會連結 | 2026-09-18 |

## 05｜這 11 個 Track 在同一張地圖的哪裡？

[閱讀本章](chapters/05-track-landscape.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html) · Ray | KubeRay Operator 與 Ray 叢集管理、位於 broader Ray project 的專案關係。；KubeRay屬於Ray整體專案並管理Kubernetes上的Ray運行 | 2026-09-18 |
| [TAIONE Fellowship Tracks](https://taione.org/fellowship/tracks) · 財團法人開源基金會 TAIONE | 11個當前Track及四種官方分類；未提供逐項遴選理由 | 2026-09-18 |
| [Apache DataFusion Comet](https://datafusion.apache.org/comet/) · Apache DataFusion | Comet在既有Spark流程中提供加速，遇不支援功能回退；不引用通用倍數 | 2026-09-18 |

## 06｜vLLM：模型已經會回答，為什麼還需要推論引擎？

[閱讀本章](chapters/06-vllm.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Welcome to vLLM](https://docs.vllm.ai/en/latest/) · vLLM | 推論與服務定位、Berkeley 起源、模型與硬體生態。；模型推論及服務、批次與記憶體管理能力；不引用自稱領先或效能倍數 | 2026-09-18 |
| [vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention](https://vllm.ai/blog/2023-06-20-vllm) · vLLM | PagedAttention 分塊管理 KV cache、連續生成時的記憶體問題；歷史效能數字未泛化。 | 2026-09-18 |
| [Accelerate AI inference with vLLM](https://www.redhat.com/en/blog/accelerate-ai-inference-vllm) · Red Hat | Red Hat 自述參與貢獻及將 vLLM 整合至有支援的企業產品。 | 2026-09-18 |
| [Governance Process](https://docs.vllm.ai/en/latest/governance/process/) · vLLM | Committer 身分屬個人、維護者責任與長期貢獻資格。；不同維護角色、個人貢獻與專案責任，以及治理權不出售 | 2026-09-18 |

## 07｜Ray：一台電腦不夠時，程式如何交給很多台一起做？

[閱讀本章](chapters/07-ray.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Ray Core Key Concepts](https://docs.ray.io/en/latest/ray-core/key-concepts.html) · Ray | Tasks、Actors、Objects 與資源需求的分散執行方式。 | 2026-09-18 |
| [Ray repository overview](https://github.com/ray-project/ray) · Ray | Ray Core 與 Data、Train、Tune、Serve 等工具的分工。 | 2026-09-18 |
| [About Anyscale](https://www.anyscale.com/about) · Anyscale | 公司自述 Ray 研究起源、2019 年創辦 Anyscale 及商業平台定位。 | 2026-09-18 |
| [Ray Governance](https://docs.ray.io/en/latest/ray-governance/index.html) · Ray | Committer、TSC、lead maintainers 的階層治理與 LF Projects 架構。 | 2026-09-18 |

## 08｜Kubernetes：服務一直要在線，誰負責把它維持住？

[閱讀本章](chapters/08-kubernetes.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/) · Kubernetes | 期望狀態、部署管理、自動恢復與可擴充介面的功能及限制。；部署、擴展、故障替換及平台功能邊界 | 2026-09-18 |
| [Kubernetes Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) · Kubernetes | 服務實例與逐步更新的管理方式。 | 2026-09-18 |
| [10 Years of Kubernetes](https://kubernetes.io/blog/2024/06/06/10-years-of-kubernetes/) · Kubernetes | Google 起源、2015 年捐贈 CNCF 與早期多公司參與。 | 2026-09-18 |
| [Kubernetes Governance](https://github.com/kubernetes/community/blob/main/governance.md) · Kubernetes | SIG、子專案責任、跨組織協作與決策程序。 | 2026-09-18 |
| [Getting started with Ray on Google Kubernetes Engine](https://cloud.google.com/blog/products/containers-kubernetes/use-ray-on-kubernetes-with-kuberay) · Google Cloud | GKE 與 KubeRay 的正式整合範例；含監控、日誌與權限。 | 2026-09-18 |

## 09｜Apache YuniKorn：大家都要算力時，誰先用、怎麼分？

[閱讀本章](chapters/09-yunikorn.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Welcome to Apache YuniKorn](https://yunikorn.apache.org/) · Apache YuniKorn | Kubernetes 排程器定位、佇列與資源公平性。 | 2026-09-18 |
| [YuniKorn Core Features](https://yunikorn.apache.org/docs/get_started/core_features/) · Apache YuniKorn | 成組排程、佇列、資源保留與多租戶公平性。 | 2026-09-18 |
| [YuniKorn: a universal resources scheduler](https://www.cloudera.com/blog/technical/yunikorn-a-universal-resources-scheduler.html) · Cloudera | 2019 年宣布開源、企業資源管理需求與早期起源；未當作現行架構完整說明。 | 2026-09-18 |
| [Cloudera Data Engineering auto-scaling](https://docs.cloudera.com/data-engineering/cloud/overview/topics/cde-auto-scaling.html) · Cloudera | Cloudera Data Engineering 採用 YuniKorn 調度；文中的 Incubating 舊字不沿用。 | 2026-09-18 |
| [Who We Are](https://yunikorn.apache.org/community/people/) · Apache YuniKorn | 個人 PMC、Committer 角色，組織背景與資格、投票責任。 | 2026-09-18 |

## 10｜KubeRay：Ray 會分工了，為什麼還需要另一個專案？

[閱讀本章](chapters/10-kuberay.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Getting started with Ray on Google Kubernetes Engine](https://cloud.google.com/blog/products/containers-kubernetes/use-ray-on-kubernetes-with-kuberay) · Google Cloud | GKE 與 KubeRay 的正式整合範例；含監控、日誌與權限。 | 2026-09-18 |
| [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html) · Ray | KubeRay Operator 與 Ray 叢集管理、位於 broader Ray project 的專案關係。；KubeRay屬於Ray整體專案並管理Kubernetes上的Ray運行 | 2026-09-18 |
| [KubeRay repository overview](https://github.com/ray-project/kuberay) · KubeRay | RayCluster、RayJob、RayService 資源分工與整合角色。 | 2026-09-18 |
| [Partnering with Anyscale to integrate RayTurbo with GKE](https://cloud.google.com/blog/products/containers-kubernetes/partnering-with-anyscale-to-integrate-rayturbo-with-gke) · Google Cloud | Google 與 Anyscale 自述共同參與開源 KubeRay；未把 RayTurbo 專屬功能當成開源能力。 | 2026-09-18 |
| [Contributing to KubeRay](https://github.com/ray-project/kuberay/blob/master/CONTRIBUTING.md) · KubeRay | 公開設計協作與文件、unit/e2e tests 的貢獻要求。 | 2026-09-18 |

## 11｜Kafka：剛發生的事，怎麼讓很多系統一起知道？

[閱讀本章](chapters/11-kafka.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Introduction](https://kafka.apache.org/intro/) · Apache Kafka | 事件發布與訂閱、保留後重讀、分區順序及資料流概念 | 2026-09-18 |
| [How LinkedIn customizes Apache Kafka for 7 trillion messages per day](https://www.linkedin.com/blog/engineering/open-source/apache-kafka-trillion-messages) · LinkedIn Engineering | 2019 年自述 Kafka 內部起源、正式環境維護分支、回饋上游及部分修補未被接受；不是目前規模或全球市占證據 | 2026-09-18 |
| [Developer Guide](https://kafka.apache.org/community/developer/) · Apache Kafka | 重大變更 KIP、測試相容性、PMC 評估 Committer 的持續貢獻與技術判斷 | 2026-09-18 |

## 12｜Ozone：資料越堆越多，底下的倉庫誰來顧？

[閱讀本章](chapters/12-ozone.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Apache Ozone](https://ozone.apache.org/) · Apache Ozone | 分散式儲存用途、S3 與 Hadoop 介面、複本、糾刪碼及權限功能 | 2026-09-18 |
| [Introduction to Ozone](https://docs.cloudera.com/cdp-private-cloud-base/7.3.2/ozone-overview/topics/ozone-introduction.html) · Cloudera | 物件與區塊、分層管理、儲存介面與容錯架構；產品文件不能代表中立比較 | 2026-09-18 |
| [Who Uses Ozone?](https://ozone.apache.org/community/who-uses-ozone/) · Apache Ozone | 官方列出的 Tencent、Shopee、Preferred Networks 與 Cloudera 採用關係；不能推論治理權或市場占比 | 2026-09-18 |
| [Ozone Write Pipeline V2 with Ratis Streaming](https://www.cloudera.com/blog/technical/ozone-write-pipeline-v2-with-ratis-streaming.html) · Cloudera | 2022 年公司工程團隊自述參與 Ozone 寫入管線改善 | 2026-09-18 |
| [How to Contribute to Apache Ozone](https://ozone.apache.org/community/how-to-contribute/) · Apache Ozone | 公開開發參與、測試、文件與問題回報的入口 | 2026-09-18 |

## 13｜DataFusion：做資料產品，查詢引擎一定要自己重寫嗎？

[閱讀本章](chapters/13-datafusion.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Introduction](https://datafusion.apache.org/user-guide/introduction.html) · Apache DataFusion | Rust、Arrow、可嵌入可擴充查詢引擎、規劃與運算能力、已知下游系統；可嵌入及延伸的查詢引擎，讓下游重用共同資料處理能力 | 2026-09-18 |
| [Query data: InfluxDB 3 Enterprise](https://docs.influxdata.com/influxdb3/enterprise/get-started/query/) · InfluxData | InfluxDB 3 SQL 以 DataFusion 為基礎並擴充時間序列功能 | 2026-09-18 |
| [Governance](https://datafusion.apache.org/contributor-guide/governance.html) · Apache DataFusion | Apache 治理、共識與商業獨立、個人角色及所屬機構，以及 Comet 子專案關係 | 2026-09-18 |

## 14｜Comet：能不能保留 Spark，用更少資源完成查詢？

[閱讀本章](chapters/14-comet.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Governance](https://datafusion.apache.org/contributor-guide/governance.html) · Apache DataFusion | Apache 治理、共識與商業獨立、個人角色及所屬機構，以及 Comet 子專案關係 | 2026-09-18 |
| [Apache DataFusion Comet overview](https://datafusion.apache.org/comet/contributor-guide/plugin_overview.html) · Apache DataFusion Comet | Spark 加速、保留查詢方式與不支援運算回退的設計方向 | 2026-09-18 |
| [Apache DataFusion Comet repository](https://github.com/apache/datafusion-comet) · Apache DataFusion Comet | 現行 Rust DataFusion 與 JVM Arrow 批次路徑、相容與版本相關說明 | 2026-09-18 |
| [Announcing Apache Arrow DataFusion Comet](https://arrow.apache.org/blog/2024/03/06/comet-donation/) · Apache Arrow PMC | 2024 年 Apple 起源與捐贈、參與工程師關係，以及擴大社群的公告意圖 | 2026-09-18 |
| [Contributing to Apache DataFusion Comet](https://datafusion.apache.org/comet/contributor-guide/contributing.html) · Apache DataFusion Comet | 正確性效能測試、補運算、審查與文件等參與方式 | 2026-09-18 |

## 15｜Airflow：每天都要跑的資料流程，誰來盯著？

[閱讀本章](chapters/15-airflow.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [What is Airflow?](https://airflow.apache.org/docs/apache-airflow/stable/index.html) · Apache Airflow | Python 工作流、排程與依賴、狀態追蹤、批次與事件觸發、重跑與補算 | 2026-09-18 |
| [Project: History](https://airflow.apache.org/docs/apache-airflow/stable/project.html) · Apache Airflow | Airbnb 2014 起源、2016 Apache 孵化、2019 頂級專案 | 2026-09-18 |
| [Community](https://airflow.apache.org/community/) · Apache Airflow | AIP 公開提案、開發郵件清單與投票、PMC 及參與方式 | 2026-09-18 |

## 16｜Flyte：AI 實驗變成長時間工作後，怎麼可靠地跑？

[閱讀本章](chapters/16-flyte.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Flyte 2 Is Here](https://flyte.org/platform/flyte-2-is-here) · Flyte / Union Team | 2026 年3月公告中的 Python 任務執行、快取、錯誤與重試概念；當時部署狀態不可當現在狀態 | 2026-09-18 |
| [Advanced composition, Flyte 1.13.3](https://docs-flyte-legacy.union.ai/en/v1.13.3/user_guide/advanced_composition/index.html) · Flyte | 舊版也有條件、dynamic workflows 與其他進階組合，不能宣稱完全靜態 | 2026-09-18 |
| [Flyte 1 vs. Flyte 2](https://flyte.org/flyte1-vs-flyte2) · Flyte / Union.ai | 兩代主要撰寫模型差異、Python 任務互叫及新 SDK；行銷對比不作效能保證 | 2026-09-18 |
| [LF AI & Data Foundation Announces Graduation of Flyte Project](https://lfaidata.foundation/blog/2022/01/20/lf-ai-data-foundation-announces-graduation-of-flyte-project/) · LF AI & Data Foundation | Lyft 開發開源起源、基金會歸屬、畢業依據與 Union 支持背景 | 2026-09-18 |
| [Flyte Governance](https://github.com/flyteorg/community/blob/main/GOVERNANCE.md) · Flyte community | Committer、Maintainer、Steering Committee 的不同責任與權限 | 2026-09-18 |
| [Flyte repository](https://github.com/flyteorg/flyte) · Flyte | 版本分支與後端狀態入口；頁面描述與網站不同處保留查核限制 | 2026-09-18 |

## 17｜現在能回答：為什麼選這 11 個嗎？

[閱讀本章](chapters/17-why-these-tracks.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html) · Ray | KubeRay Operator 與 Ray 叢集管理、位於 broader Ray project 的專案關係。；KubeRay屬於Ray整體專案並管理Kubernetes上的Ray運行 | 2026-09-18 |
| [TAIONE Fellowship 計畫介紹](https://taione.org/fellowship/about) · 財團法人開源基金會 TAIONE | 計畫意圖、Track Lead帶領、Code Review與架構討論、上游成果紀錄 | 2026-09-18 |
| [TAIONE Fellowship Tracks](https://taione.org/fellowship/tracks) · 財團法人開源基金會 TAIONE | 11個當前Track及四種官方分類；未提供逐項遴選理由 | 2026-09-18 |
| [Apache DataFusion Comet](https://datafusion.apache.org/comet/) · Apache DataFusion | Comet在既有Spark流程中提供加速，遇不支援功能回退；不引用通用倍數 | 2026-09-18 |

## 18｜多一些維護者，台灣究竟能多出什麼能力？

[閱讀本章](chapters/18-maintainers-and-taiwan.md)

| 來源 | 能支持什麼 | 查核日 |
| --- | --- | --- |
| [Governance Process](https://docs.vllm.ai/en/latest/governance/process/) · vLLM | Committer 身分屬個人、維護者責任與長期貢獻資格。；不同維護角色、個人貢獻與專案責任，以及治理權不出售 | 2026-09-18 |
| [Contributing to the Apache Software Foundation](https://community.apache.org/contributors/) · Apache Software Foundation | 文件設計等非程式貢獻、持續品質與Committer邀請；各專案程序有差異 | 2026-09-18 |
| [TAIONE 基金會簡介](https://taione.org/about/intro) · 財團法人開源基金會 TAIONE | 人才、國際Committer與治理角色、技術自主與產業連結的官方目的 | 2026-09-18 |

## 維護本書

更正內容時，請同時提供可支持更正的第一手來源、適用版本與日期。PNG 是固定呈現的閱讀版，SVG 是可編輯的向量原圖；每圖的文字稿保存在 [圖解資料](sources/figures.json)。

[← 最後一章](chapters/18-maintainers-and-taiwan.md) · [回總目錄](README.md#閱讀目錄)
