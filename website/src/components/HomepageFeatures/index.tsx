import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Projects thực chiến',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Học theo case thật: churn analysis, stock screener, segmentation.
        Mỗi project có notebook, báo cáo và link truy cập nhanh tới mã nguồn.
      </>
    ),
  },
  {
    title: 'Datasets sẵn sàng phân tích',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Có Data Dictionary, hướng dẫn tiền xử lý và link tải trực tiếp CSV để
        bạn bắt đầu EDA hoặc modeling trong vài phút.
      </>
    ),
  },
  {
    title: 'Thư viện Ebooks nổi bật',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Kho tài liệu lớn theo từng chủ đề: Python, SQL, ML, Deep Learning,
        Mathematics. Mở online hoặc tải xuống chỉ bằng một lần bấm.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
