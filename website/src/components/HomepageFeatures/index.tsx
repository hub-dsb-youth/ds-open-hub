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
    title: 'Projects thực hành',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Tổng hợp các bài toán phân tích dữ liệu, churn prediction và stock
        screening với notebook, báo cáo và ứng dụng demo.
      </>
    ),
  },
  {
    title: 'Datasets có mô tả rõ ràng',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Mỗi bộ dữ liệu đều có phần Data Dictionary, lưu ý tiền xử lý và gợi ý
        bài toán để học tập nhanh hơn.
      </>
    ),
  },
  {
    title: 'Ebook theo từng mảng',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Kho ebook lớn theo chủ đề như Data Science, Machine Learning, Python,
        SQL và Toán học phục vụ tự học dài hạn.
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
