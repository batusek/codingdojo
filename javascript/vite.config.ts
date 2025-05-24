import { defineConfig } from 'vite'

export default defineConfig({
  test: {
    reporters: ['default'],
    fileParallelism: false,
  },
})
