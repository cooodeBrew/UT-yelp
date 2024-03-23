import { initializeAuthProxy } from '@propelauth/auth-proxy'

// Replace with your configuration
await initializeAuthProxy({
    authUrl: "https://72027091.propelauthtest.com",
    integrationApiKey: "122c53ac14528fe26f3975fcbd480427dce11ac656ff143aec236fd0da851cff31e3bc19b93847dba976f182fd838c8a",
    proxyPort: 8502,
    urlWhereYourProxyIsRunning: 'http://localhost:8502',
    target: {
        host: 'localhost',
        port: 8501,
        protocol: 'http:'
    },
})
