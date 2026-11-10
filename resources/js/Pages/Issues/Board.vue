<script setup lang="ts">
import { router, useForm } from '@inertiajs/vue3'

type User = { id: number, name: string }
type Issue = { id: number, key: string, title: string, status: string, priority: string, assignee: User | null, transitions: string[] }
type Project = { id: number, key: string, name: string }

const props = defineProps<{ project: Project, issues: Issue[], users: User[] }>()

const columns = { todo: 'To Do', in_progress: 'In Progress', in_review: 'In Review', done: 'Done' }

const form = useForm({ title: '', reporter_id: props.users[0]?.id })

function addIssue() {
    form.post(`/projects/${props.project.id}/board`, { onSuccess: () => form.reset('title') })
}

function move(issue: Issue, status: string) {
    router.post(`/issues/${issue.id}/transitions`, { status }, { preserveScroll: true })
}

function remove(issue: Issue) {
    router.delete(`/issues/${issue.id}`, { preserveScroll: true })
}
</script>

<template>
    <main class="mx-auto max-w-6xl p-8">
        <h1 class="text-3xl font-semibold">{{ project.name }}</h1>

        <form class="mt-6 flex gap-2" @submit.prevent="addIssue">
            <input v-model="form.title" class="flex-1 rounded border p-2" placeholder="What's the issue?">
            <select v-model="form.reporter_id" class="rounded border p-2">
                <option v-for="user in users" :key="user.id" :value="user.id">{{ user.name }}</option>
            </select>
            <button class="rounded bg-emerald-700 px-4 text-white" :disabled="form.processing">Add</button>
        </form>
        <p v-if="form.errors.title" class="mt-2 text-sm text-red-600">{{ form.errors.title }}</p>

        <div class="mt-8 grid grid-cols-4 gap-4">
            <section v-for="(label, status) in columns" :key="status" class="rounded bg-stone-100 p-3">
                <h2 class="font-medium">{{ label }}</h2>
                <article
                    v-for="issue in issues.filter(issue => issue.status === status)"
                    :key="issue.id"
                    class="mt-3 rounded border bg-white p-3"
                >
                    <p class="text-xs text-stone-500">{{ issue.key }} · {{ issue.priority }}</p>
                    <p class="mt-1">{{ issue.title }}</p>
                    <p class="mt-1 text-xs text-stone-500">{{ issue.assignee?.name ?? 'Unassigned' }}</p>
                    <div class="mt-2 flex flex-wrap gap-2 text-sm">
                        <button
                            v-for="next in issue.transitions"
                            :key="next"
                            class="text-emerald-700"
                            @click="move(issue, next)"
                        >
                            → {{ columns[next] }}
                        </button>
                        <button class="ml-auto text-red-600" @click="remove(issue)">Delete</button>
                    </div>
                </article>
            </section>
        </div>
    </main>
</template>
