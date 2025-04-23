module.exports = {
  appId: 'com.definexus',
  productName: 'DeFiNexus',
  directories: { output: 'dist' },
  files: ['build/**/*', 'electron/**/*.js'],
  mac: { target: 'dmg' },
  win: { target: 'nsis' },
};
