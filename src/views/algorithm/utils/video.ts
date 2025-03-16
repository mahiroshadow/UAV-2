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
		flvPlayer.attachMediaElement(mountedDom)
		flvPlayer.load()
		flvPlayer.play()
		return flvPlayer
	}
}

const destroyVideo = (flvPlayer: ReturnType<typeof mpegts.createPlayer>) => {
	flvPlayer.pause()
	flvPlayer.unload()
	flvPlayer.detachMediaElement()
	flvPlayer.destroy()
}

export { createVideo, destroyVideo }
