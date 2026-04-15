import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'DS Open Hub',
  tagline: 'Knowledge Hub for Data Science Learning and Research',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: process.env.DOCS_URL || 'https://hub-dsb-youth.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: process.env.DOCS_BASE_URL || '/ds-open-hub/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: process.env.GITHUB_OWNER || 'hub-dsb-youth',
  projectName: process.env.GITHUB_REPO || 'ds-open-hub',

  onBrokenLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'vi',
    locales: ['vi', 'en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: 'docs',
          editUrl: 'https://github.com/hub-dsb-youth/ds-open-hub/tree/main/website/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'DS Open Hub',
      logo: {
        alt: 'DS Open Hub Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'hubSidebar',
          position: 'left',
          label: 'Docs',
        },
        {to: '/docs/projects', label: 'Projects', position: 'left'},
        {to: '/docs/datasets', label: 'Datasets', position: 'left'},
        {
          href: 'https://github.com/hub-dsb-youth/ds-open-hub',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'DS Open Hub',
          items: [
            {
              label: 'Giới thiệu',
              to: '/docs/intro',
            },
            {
              label: 'Projects',
              to: '/docs/projects',
            },
          ],
        },
        {
          title: 'Cộng đồng',
          items: [
            {
              label: 'Facebook Đoàn khoa',
              href: 'https://www.facebook.com/doankhoakhdltkd',
            },
            {
              label: 'Email liên hệ',
              href: 'mailto:doan.khdltkd@hub.edu.vn',
            },
          ],
        },
        {
          title: 'Nguồn',
          items: [
            {
              label: 'Repository',
              href: 'https://github.com/hub-dsb-youth/ds-open-hub',
            },
            {
              label: 'Hướng dẫn deploy',
              to: '/docs/deployment',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} DS Open Hub. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
