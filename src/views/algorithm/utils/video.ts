import mpegts from 'mpegts.js'
const createVideo = (mountedDom: HTMLVideoElement, stream: string) => {
	if (mpegts.isSupported()) {
		const flvPlayer = mpegts.createPlayer(
			{
				type: 'flv',
				isLive: true,
				hasAudio: false,
				cors: true,
				url: stream
			},
			{
				enableWorker: true,
				enableStashBuffer: false,
				stashInitialSize: 128,
				lazyLoad: false,
				lazyLoadMaxDuration: 0.2,
				deferLoadAfterSourceOpen: false,
				liveBufferLatencyChasing: true,
				liveBufferLatencyMaxLatency: 0.9,
				liveBufferLatencyMinRemain: 0.2
			}
		)
		mountedDom.addEventListener('loadeddata', function () {
			const frameRate = Math.round(mountedDom.duration / mountedDom.currentTime)
			mountedDom.textContent = '视频帧率：' + frameRate
			console.log(mountedDom.textContent)
		})
		// flvPlayer.on(mpegts.Events.STATISTICS_INFO, (statisticsInfo) => {
		//   console.log(statisticsInfo)
		// })
		// mpegts
		flvPlayer.attachMediaElement(mountedDom)
		flvPlayer.load()
		flvPlayer.play()
	}
}

export { createVideo }
